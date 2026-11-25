# Downloading models

The Provider Client downloads each model at the exact **commit** Flockadoo approved, with Hugging Face's own `hf` tool, into the standard Hugging Face cache. The engine then starts offline on that commit. It never downloads a model by itself, so an upstream change on Hugging Face cannot change what you serve.

## When a model is downloaded

You rarely need to download by hand. The client downloads the approved commit:

- in the [setup wizard](setup.md), after you agree to start the engine and before it starts;
- when the client starts and the commit it serves is not on disk yet;
- on a [Team Flock](../provider/team-flocks.md), on every machine, before the client shows the command to start the engine.

You see `hf`'s own progress. A 20 to 60 GB model can take a while.

## Commands

| Command | What it does |
|---|---|
| `flockadoo model download` | Download the configured model at its current approved commit |
| `flockadoo model download <alias>` | Download another approved model. Your configured model does not change |
| `flockadoo model download --revision <commit>` | Download a specific approved commit (current or accepted) |
| `flockadoo model list` | Show the approved models on disk: commit, status, size and the last verification result |
| `flockadoo model verify [alias]` | Check the model on disk with Flockadoo now, before you start the engine |
| `flockadoo model login` | Log in to Hugging Face, for gated models only |

For example:

```bash
flockadoo model download Qwen/Qwen2.5-7B-Instruct
flockadoo model list
```

```
MODEL                     COMMIT                                    STATUS    SIZE     LAST VERDICT
Qwen/Qwen2.5-7B-Instruct  a09a35458c702b33eeacc393d103063234e8bc28  current   15.2 GB  verified 2026-11-24 09:12
```

`model list` reads file sizes only. It does not hash anything, so it is quick. The status comes from the folder name, and the last verdict from the last time Flockadoo checked it. To check the files now, run `flockadoo model verify`.

When `model download` fetches the model you serve, it remembers the commit in `config.yaml`. Restart the client to serve it.

## Where models go

Models go into the standard Hugging Face cache, the same folder `hf`, vLLM and Python's `huggingface_hub` use:

| If set | Folder |
|---|---|
| `HF_HUB_CACHE` | that folder |
| `HF_HOME` | `$HF_HOME/hub` |
| otherwise | `~/.cache/huggingface/hub` (`XDG_CACHE_HOME` moves `~/.cache`) |

A model you downloaded before installing Flockadoo is reused when it is at an approved commit, and a model Flockadoo downloads is usable by your other tools. The client logs the folder it uses when it starts.

**To use a bigger disk,** set `HF_HUB_CACHE` in the environment the client runs in, for example `HF_HUB_CACHE=/data/huggingface/hub`.

!!! warning

    The `hf_hub_cache` option in `config.yaml` is going away. It only told the verifier where to look, not `hf` or the engine. The client warns when it is set. Remove it and set `HF_HUB_CACHE` instead.

Run `flockadoo model download` as the same user that runs the client. Run as root without `HF_HUB_CACHE`, it refuses: the model would land in root's home, where the client never looks.

## Disk space

Before a download starts, the client checks the free space on the disk that holds the cache. It needs the model's size plus **10%**, and at least **2 GB** spare. If there is not enough, it stops before downloading and says how much it needs, how much is free, and where.

`flockadoo model download --skip-space-check` downloads anyway. Files already in the cache are reused: a new commit that changes one tokenizer file downloads only that file.

## Current, accepted and retired

When a model's publisher fixes something upstream (a chat template, a tokenizer), Flockadoo may approve the new commit. Each model then has:

| Status | What it means for you |
|---|---|
| **current** | What new downloads get |
| **accepted** | The commit before current. You keep serving it, and you keep getting requests |
| **retired** | Older. Flockadoo no longer routes requests to it |

When a new commit becomes current, the old current one becomes accepted and the one before that is retired. So you can be one commit behind without doing anything.

- **On the accepted commit,** the client says at start that a newer commit is current. Download it with `flockadoo model download` when it suits you, then restart.
- **On a retired commit,** the client says so and keeps it. It does **not** download the current one by itself, because that can be a large download. Run `flockadoo model download`, then restart.

## Gated models

Some Hugging Face repos need you to accept a licence. When a download is refused for that reason, the client walks you through it:

1. Create a Hugging Face account at [huggingface.co/join](https://huggingface.co/join), if you have none.
2. Open the model's page on Hugging Face and accept its licence. Some publishers approve requests by hand, which can take a while.
3. Create a **read** token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
4. Run `flockadoo model login` and paste the token at Hugging Face's prompt.

Then run the download again. The token goes from you to Hugging Face's own tool, which keeps it where `hf` and vLLM find it. Flockadoo never reads, stores or sends it. If you already use `hf auth login` or set `HF_TOKEN`, that works as it is.

## Team Flocks

Every machine in a flock serves the same commit, because machines with different weights would give wrong answers. Flockadoo names it: the commit the master serves, while it is still approved. Each machine downloads it, with its own Hugging Face login if the model needs one, before the client shows the engine command. When a new commit is approved, a running flock keeps its commit. It moves only once the master's commit is retired.

## Running the engine yourself

If you start vLLM yourself, start it on the approved commit, offline, so it never downloads `main`:

```bash
flockadoo model download
HF_HUB_OFFLINE=1 vllm serve Qwen/Qwen2.5-7B-Instruct \
  --revision a09a35458c702b33eeacc393d103063234e8bc28 \
  --tokenizer-revision a09a35458c702b33eeacc393d103063234e8bc28 \
  …the other flags setup prints
```

The commit is in `config.yaml` as `hf_revision` after a download, and in the [catalog](approved-models.md) under `revisions`. The command `flockadoo setup` prints already has it.

For llama.cpp, serve the cached file of that commit with `-m`, for example `-m ~/.cache/huggingface/hub/models--Qwen--Qwen2.5-7B-Instruct-GGUF/snapshots/<commit>/<gguf_file>`.

## Related

- [Setup wizard](setup.md)
- [Approved model builds](approved-models.md)
- [Configuration](configuration.md)
- [Team Flocks](../provider/team-flocks.md)
