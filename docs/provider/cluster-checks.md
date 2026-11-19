# Engine checks

When the provider client starts your engine, it checks what the engine can do and measures how many requests it can serve at once. Inferoute routes on these results: a request that needs a capability goes only to clusters that passed it.

You can see the results on the cluster page:

| Where | What you see |
| --- | --- |
| **Overview** tab, **Engine checks** card | Each capability's result, whether the model is verified, and how many requests the cluster takes at once |
| **Checks** tab | The full record: the model and its build, what each result means for you, and every benchmark level |

The results are what your own client reported. The owner and the workers of a cluster can both see them.

## Open the Checks tab

1. Click **Clusters** in the sidebar.
2. Open the cluster.
3. Open **Checks**, or click **Details** on the **Engine checks** card.

## Capabilities

| Capability | Requests that need it |
| --- | --- |
| **Tool calling** | Requests that send `tools` |
| **Forced tool choice** | Requests whose `tool_choice` names a function or is `"required"` |
| **Reasoning** | Every request for a model that thinks (see below) |
| **JSON schema** | Requests with `response_format` type `json_schema` |
| **JSON mode** | Requests with `response_format` type `json_object` |
| **Logprobs** | Requests that ask for `logprobs` |

Each capability shows one result:

| Result | Meaning |
| --- | --- |
| **Supported** | The engine passed the check. You get requests that need it. |
| **Not supported** | The engine answered, and it cannot do this. Requests that need it go to other clusters. |
| **Not for this model** | The model's build does not allow it. For example, a model that does not think has nothing to check for **Reasoning**. |
| **Couldn't check · retrying** | The check timed out or the engine errored. The client tries again while the GPU is idle. |
| **Checking** | The client is checking it now, after the engine or model changed. |
| **Not checked yet** | The client has not reported this check yet. |

Until a capability is **Supported**, requests that need it go to other clusters. Ordinary requests keep coming in the meantime.

!!! warning

    **Reasoning** is stricter than the others. A model that thinks (Qwen3, DeepSeek-R1, gpt-oss, Gemma 4) is served only by clusters whose engine sends the thinking apart from the answer. Until **Reasoning** is **Supported**, your cluster gets no requests for that model at all.

An embedding model gets no chat checks. The tab says **Chat checks do not apply to an embedding model.**

## Model

The **Model** panel shows the model the cluster serves now:

- **Verified** means the model is an approved build and its weights header matched. Your own price applies only after this. See [Model pricing](model-pricing.md).
- **Tool parser** and **Reasoning parser** come from the approved build. A model without a tool parser cannot take tool requests, so **Tool calling** shows **Not for this model**.

Other models your client has registered on the cluster are listed below, with whether each is verified.

## Concurrency benchmark

The client sends 1, 2, 4, 8 and then 16 requests at once. It stops at the first level that fails or gets too slow, and takes the highest level that held up. The cluster then takes that many requests at once.

| Result | Meaning |
| --- | --- |
| **Passed** | This level held up. |
| **In use** | The number of requests the cluster takes at once. |
| **Did not pass** | The level where the client stopped. |

For example, **inferoute-cluster1** shows **8 requests at once** when 8 held up and 16 did not.

If even one request at a time failed, nothing was measured. The card then says **Not measured**, and the cluster takes a starting number until a benchmark completes.

## Related

- [How the client works](../provider-client/how-it-works.md)
- [Supported parameters](../consumer/supported-parameters.md)
- [Model pricing](model-pricing.md)
