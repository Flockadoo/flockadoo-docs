# FAQ

## General

### How do I get started as a provider?

1. Check [Software and hardware requirements](../getting-started/requirements.md).
2. [Sign up and create a flock](../getting-started/signup.md) to copy a provider API key.
3. [Install the client](../getting-started/installation.md). The [setup wizard](setup.md) installs the LLM engine and an approved model — you do not need the engine already running.

### What is the Flockadoo Provider Client?

A lightweight service that runs next to a local LLM engine (vLLM, vLLM Metal, or llama.cpp). It monitors GPU resources, reports health to Flockadoo, and handles inference requests by forwarding them to that engine.

### What platforms are supported?

- **Linux with NVIDIA GPU:** At least **32 GB** of system memory and **24 GB** of VRAM. vLLM. The health report includes utilization. See [Setup: Linux](setup-linux.md).
- **macOS with Apple Silicon:** At least **48 GB** of unified memory for approved vLLM Metal models. The wizard also offers llama.cpp. Intel Macs are not supported. Basic GPU info (model, core count). Utilization is not reported. A request in flight still marks the client busy. See [Setup: macOS](setup-mac.md).
- **Windows amd64:** **32 GB** of RAM plus a **fixed 64 GB page file** (or **64 GB** of RAM), and an NVIDIA GPU with **24 GB** of VRAM. llama.cpp only. It only lists catalog rows tagged `llama_cpp`. Encoder and embedding models such as `baai/bge-m3` stay off Windows. GPU monitoring via `nvidia-smi` when the NVIDIA driver is installed. See [Setup: Windows](setup-windows.md).

### How do I configure the client?

Prefer **`flockadoo setup`**. It writes engine, model, and API key into the YAML config. Server and logging stay in that file — see [Configuration](configuration.md). The connection to Flockadoo is opened at startup — it is not a config section.

### How do I update the client?

Stop the client, run `flockadoo update`, then start it again. The console tells you when a newer release exists. If it says **Update required**, Flockadoo is no longer accepting that release. See [Updating the client](updating.md).

### Can I earn while capability checks run?

Yes, from ordinary inference requests, if consumers send them. The checks decide whether you can also receive requests that need tools, JSON mode, or logprobs. Being online does not by itself guarantee traffic.

### Why does a capability stay unverified?

The check did not finish. A timeout, an engine error, or a cancelled check is unverified, not a "no". The client retries while the GPU is idle: after 1 minute, 5 minutes, 30 minutes, then hourly.

### Why do capability checks run again?

They run again when the deployment changes: model, engine, engine version, weights, context length, GPU, node count, tool parser, or engine arguments. A late result from the previous deployment is dropped.

### How do I change engine or model later?

Stop the engine if it is already running, then re-run the [setup wizard](setup.md):

```bash
flockadoo setup
```

Auto-start only replays `config.yaml`. It does not notice that the catalog row changed, and it will not restart a process that is already listening.

### Can I start vLLM (or llama.cpp) myself?

Yes. Use the same flags the wizard printed. If the catalog row has no `tool_call_parser`, do not pass `--enable-auto-tool-choice` (vLLM) or `--jinja` (llama.cpp). If the catalog sets `max_model_len`, serve at least that context or verification fails. Memory and batching flags, such as `--gpu-memory-utilization` and `--max-num-seqs`, are fine as long as the live context stays at least the catalog `max_model_len`. Safer: let setup start the engine. See [Which flags change verification](approved-models.md#which-flags-change-verification).

### Setup says this machine's GPU differs from the master

The worker GPU is not the same model as the master's. Setup prints the two names and continues. Flockadoo tests flocks where every machine has the same GPU. Mixing can work, and it can also leave vLLM stuck during startup. Use the same GPU when you can. See [GPUs across nodes](../provider/team-flocks.md#gpus-across-nodes).

### Setup wants to reinstall vLLM

There are two reasons.

- **The release is older than 0.30.0.** Setup prints **Flockadoo needs vLLM 0.30.0 or newer**. Say yes and setup installs the current release. Say no and setup leaves the old release in place, turns **auto_start** off, and the client does not serve through it. See [Supported engine versions](setup.md#supported-engine-versions).
- **The flock pins another release.** The flock owner set a **vLLM version** on **Nodes**, and this machine has a different release. Pipeline parallel needs the same vLLM on every machine. Say yes and setup removes `~/.venv-vllm` and installs the pinned release. Say no and setup leaves the old release in place. The flock may not start.

A reinstall takes several minutes. A worker install does not ask. `--yes` also accepts the reinstall.

### "older than Flockadoo supports (vLLM 0.30.0 or newer)"

The vLLM or vLLM Metal that is running is older than 0.30.0. Until it is upgraded, the client offers no models to Flockadoo and refuses requests that reach it, so you earn nothing from this machine. Stop the engine and run `flockadoo setup`; it installs the current release. vLLM before 0.30 handles the long-context (YaRN) settings differently and would serve some models past their limit with wrong output.

### "needs about … to start; … is free"

The client checked the model against the memory free right now and did not start the engine, because the model would not fit. For example:

```
Qwen/Qwen2.5-14B-Instruct needs about 14.80 GiB to start at a 32,768-token context; 10.00 GiB of GPU memory is free.
```

The need is the model's weights plus room for one request at the model's full context. On a machine whose GPU shares memory with the CPU, such as a DGX Spark (GB10), vLLM may use only a share of the memory; see [What is the Memory share line?](#what-is-the-memory-share-line).

To start the model, free memory, then start the client again:

- **Close other programs that use the GPU.** On a GB10 or a Mac, that includes desktop apps and browsers, because they use the same memory. On Linux, `nvidia-smi` lists the processes using a dedicated GPU.
- **Stop leftover vLLM engine processes.** If the client found any, the message names them with the command to stop them. See ["A vLLM engine process with no API server is holding memory"](#a-vllm-engine-process-with-no-api-server-is-holding-memory).
- **Or choose a smaller model** with `flockadoo setup`. `flockadoo compatibility` shows which models fit this machine.

Do not lower the context below the catalog's `max_model_len`. The model would start, but verification fails and Flockadoo does not route to it. See [Which flags change verification](approved-models.md#which-flags-change-verification).

When the client cannot tell, it starts the engine as before. That is the case on a Mac, which does not report free memory yet, with several GPUs, on a Team Flock, or when the model catalog cannot be read.

### "vLLM did not start: it asks for … and only … is free"

vLLM reserves a share of the GPU's total memory when it starts, 0.92 by default, and refuses to start if that much is not free. The client found vLLM's refusal in the engine log and shows its numbers. For example:

```
vLLM did not start: it asks for 112.11 GiB (0.92 of the 121.86 GiB on cuda:0) and only 105.25 GiB is free.
```

- **Dedicated GPU:** another program is using GPU memory. Check `nvidia-smi`, and close it.
- **GB10:** from client 0.48.0, the client gives vLLM a share that fits the free memory. If you still see this, check that `engine_args` in your config does not set its own `--gpu-memory-utilization`. The client keeps a value you set.

### "vLLM ran out of memory on this Mac's GPU"

vLLM Metal ran out of memory while it loaded the model. The CPU, macOS and every app share the Mac's memory. Close other apps, stop leftover vLLM engine processes, or choose a smaller model.

### "A vLLM engine process with no API server is holding memory"

vLLM runs as two processes: the server that takes requests, and an engine process called `VLLM::EngineCore`. If the server is killed hard (`kill -9`, the system running out of memory, a crash), the engine process can keep running and keep its memory. It cannot serve anything.

Before it starts an engine, the client looks for such processes of your user. It never stops one, because it could be yours to keep. It shows the process with its memory, its age and the command to stop it. For example:

```
A vLLM engine process with no API server is holding memory (pid 41467, 5.8 GiB, running 7 days 18 hours). It is probably left over from a vLLM that was killed. If it is not yours to keep, stop it with: kill 41467
```

The same line is on the status page as **Orphaned engines**. To look at the process first:

```bash
ps -o pid,ppid,etime,rss,command -p 41467
```

If `kill` does not stop it within a few seconds, use `kill -9 41467`. A vLLM that is running normally, however you started it, is never reported.

### What is the Memory share line?

On a machine whose GPU shares memory with the CPU, such as a DGX Spark (GB10), the status page shows **Memory share**. For example, `0.81 of 121.86 GiB, chosen at start (105.25 GiB was free)`.

vLLM's default asks for 0.92 of the total memory. With a desktop running, that much is rarely free, and vLLM refuses to start. So right before each start, the client gives vLLM the share that fits the free memory, minus a margin for the system (4 GiB or 5%, whichever is larger).

- **The share can change between starts.** A smaller share means room for fewer requests at once. If it drops by more than 0.05, the client lowers its concurrency limit and benchmarks again.
- **To fix the share yourself,** put `--gpu-memory-utilization` in `engine_args`. The line then says **set in the engine command**.
- **No line** on a dedicated GPU, a Mac, or llama.cpp: those start as before.

### vLLM crashes at startup with "Could not find nvcc"

vLLM tried to compile the FlashInfer sampling kernel on first start. The machine has a GPU driver and no CUDA compiler (`nvcc`). Rented GPU boxes often look like this.

`download-kernels` installs other FlashInfer kernels. It does not install this sampler. Setup still runs it on a new install. If vLLM was already installed, run it once yourself:

```bash
~/.venv-vllm/bin/python -m flashinfer download-kernels
```

On a machine with no `nvcc`, put this in front of the command setup printed. Set it on every machine in the flock:

```bash
VLLM_USE_FLASHINFER_SAMPLER=0
```

For example, `VLLM_USE_FLASHINFER_SAMPLER=0 vllm serve ...`. Sampling is a little slower.

A machine with the CUDA toolkit installed can compile the sampler instead, so skip the variable there. `nvcc --version` has to succeed for the user that starts vLLM. The first start takes longer. Later starts reuse the compiled sampler. On a GPU with compute capability **10.0** or higher, install CUDA **12.9** or newer. Check the toolkit with `nvcc --version`. The CUDA version printed by `nvidia-smi` is the driver.

On a Team Flock, one crashed machine leaves the others waiting. The master often logs `No available shared memory broadcast block found in 60 seconds` while a worker is still compiling, or stuck waiting for that machine. That line is the wait. The worker crash is the failure. Stop vLLM on every machine, then start the master, then the workers. See [Team Flocks](../provider/team-flocks.md).

### Why winglink and not Tailscale?

Tailscale gives every machine an address from one fixed range, `100.64.0.0/10`. That range is built into the program. If setup used Tailscale for the flock network, it would collide with a Tailscale network you already run on the same machine: the same addresses, the same network device, the same routes.

So Flockadoo ships **winglink**, its own version of Tailscale. It uses a different range, `198.18.0.0/15`, and its own network device, `winglink0`. Your Tailscale keeps working and the two stay out of each other's way. For example, a machine can stay on your own tailnet at `100.x.x.x` and join **flockadoo-flock1** at `198.18.x.x`.

You do not install it yourself. Setup downloads and starts it. See [How the machines connect](../provider/team-flocks.md#how-the-machines-connect).

### Setup asks for my password (`winglink0`)

Team Flock setup joins a private network. It prints `winglink needs root to create winglink0` and runs `sudo`. Enter your password. If the machine has no `sudo`, setup stops with `winglink needs root to create winglink0, and sudo is not installed`. This step runs on Linux only. See [How the machines connect](../provider/team-flocks.md#how-the-machines-connect).

### "one-shot key was rejected" or "one-shot key was already used"

This machine is not on the private network, and the one-shot network key is gone.

On the **master**, run `flockadoo setup` again. Setup requests a new key.

On a **worker**, the join code was spent. Ask the owner for a **New code**. Then run:

```bash
flockadoo setup --api-key "join-…"
```

`flockadoo setup` alone prints `This machine is already in the flock.` and will not ask for the new code.

### Can I move a machine to another flock?

Yes. Run `flockadoo setup --api-key "…"` with the new flock's join code or provider API key. Setup logs the machine out of the old private network before it joins the new one. You do not need to clean anything up by hand.

If the machine still shows the old address after setup, log out yourself and run setup again:

```bash
sudo /usr/local/libexec/flockadoo/winglink logout
flockadoo setup --api-key "…"
```

### "the owner removed this machine from the flock"

The owner clicked **Remove** on **Nodes**. Run `flockadoo setup` and paste a new join code. See [Joining a flock](../provider/joining-a-flock.md).

### How do I delete a flock from my account?

Use the dashboard: **My Flocks** → select your flock → **Settings** → **Delete flock** (Danger zone). That stops inference and revokes API keys; it does not uninstall the client on your machine. See [Deleting and managing flocks](../provider/deleting-flocks.md).

## Model management

### When I add new models, does the client pick them up?

Yes. New models are detected on each health check (every **3 minutes**). The client advertises at most 5 approved models per flock. Marketplace routing still requires an [approved model build](approved-models.md). Re-run setup to switch the engine to a different approved model.

### How does model pricing work?

Pricing is **per flock**, not account-wide. A new model starts at the market-average price. You can change it once the model shows **Verified**, whether or not it shows **Serving**. A model that shows **Not verified** keeps the market-average price. For example, **flockadoo-flock1** and **flockadoo-flock2** can charge different prices for the same model name.

The client advertises at most 5 approved models. Each model has a maximum price.

See [Model pricing](../provider/model-pricing.md) for editing prices in the dashboard.

### Can I change model pricing after registration?

Yes, once the model shows **Verified**. Open **My Flocks** → select a flock → **Models** tab. You can also call `PATCH /api/provider/models/{model_id}/pricing` on `https://core.flockadoo.ai` with that flock’s provider API key. Prices are $/1M with up to 2 decimals. See [Model pricing](../provider/model-pricing.md).

Changing prices on one flock does not change another. See [Model pricing](../provider/model-pricing.md).

### Which models are approved on the marketplace?

See [Approved model builds](approved-models.md). Call **GET** `/api/models/approved-builds` for the public catalog (aliases, HuggingFace locations, and `engines`; no hashes). The setup wizard lists rows tagged for this engine that should also fit this machine. On Windows, models without `llama_cpp` in `engines` are hidden. The dashboard says **No Windows build yet**.

## Reaching your machine

### Do I set a public URL?

No. On startup the client opens an outbound connection to Flockadoo. Flockadoo sends inference requests back over that connection. You do not install another program or open inbound ports.

### What if the connection drops?

The client reconnects on its own. Check the client logs if it stays disconnected.

### Can other providers SSH into my machine?

No, not over the private network a Team Flock uses. Port **22** is blocked there. That does not mean the other node is safe. Only share a flock with people you intend to share GPUs with. See [Team Flock networking](../provider/Team Flock-networking.md).

### What can other nodes in a Team Flock reach?

vLLM on **8000**, llama.cpp on **8081**, the distributed setup port **29501**, ping, and TCP **32768–60999** for GPU-to-GPU traffic. SSH, typical web admin, and database ports stay closed. The high-port window is wide on purpose. A service you bind there on all interfaces is reachable by every node in the flock. See [Team Flock networking](../provider/Team Flock-networking.md).

### The client failed to start because of the API key

The provider API key in **config.yaml** (`api_key`) must be the key for **that flock**, copied from **My Flocks** → select the flock → **Settings**. A consumer key, an old rotated key, or a typo is rejected at startup with an “Invalid provider API key” message.

For example, after you regenerate the key in **Settings**, update `api_key` (or re-run setup) and restart the client. Do not leave the placeholder `your_api_key_here`.

## Health and monitoring

### How often does the client report health?

Every **3 minutes**, and also when the client becomes busy or free. It exposes **GET /api/health** for on-demand status.

### What is in a health report?

- GPU info (type, driver, CUDA, memory, utilization where available).
- Available models from the local LLM server.
- Whether the client is connected to Flockadoo.

Flock **country** is not part of the health payload. Flockadoo resolves it from your connection. See [Flock location](../provider/flock-location.md).

### How is “GPU busy” determined?

There are two signals. See [How it works](how-it-works.md).

- **Rejecting a new request** (`GET /api/busy` and **503**): every inference slot is full. The default is one request at a time.
- **Health report** GPU `is_busy`: on Linux and Windows with NVIDIA, utilization above **20%**, or a slot is full. On macOS, a slot is full.
- No GPU monitoring and nothing in flight: the health report does not mark the GPU busy from utilization.

## Inference requests

### How are inference requests handled?

1. The request signature in `X-Request-Id` is validated with Flockadoo; missing or invalid requests get **401**.
2. If every inference slot is full → **503** `{"error":"GPU is busy"}` (Flockadoo can try another provider). Same-session follow-ups can wait for the slot instead. The **20%** utilization flag is on the health report.
3. Valid requests are proxied to the local LLM server.

### What endpoints does the client expose for inference?

OpenAI-compatible:

- **POST /v1/chat/completions**
- **POST /v1/completions**
- **POST /v1/embeddings**

## Logging

### How do I configure logging?

In `config.yaml`, under **logging:** set level (`debug`, `info`, `warn`, `error`), `log_dir`, `max_size`, `max_backups`, `max_age`. See [Configuration](configuration.md). Engine stdout from auto-start goes to **engine.log**.

### What if GPU monitoring isn’t available?

The client still runs. Health reports omit GPU utilization, so that flag stays clear unless a request is in flight. You can monitor activity via the console UI and log files.

## Related

- [Setup wizard](setup.md)
- [Installation](../getting-started/installation.md)
- [How it works](how-it-works.md)
- [Approved model builds](approved-models.md)
- [Model pricing](../provider/model-pricing.md)
- [Deleting and managing flocks](../provider/deleting-flocks.md)
- [Team Flocks](../provider/team-flocks.md)
- [Joining a flock](../provider/joining-a-flock.md)
