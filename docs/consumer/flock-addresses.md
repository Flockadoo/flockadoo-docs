# Using a flock address

Some providers give you their own address, such as `flockadoo-flock1.flock.flockadoo.ai`. It works like `core.flockadoo.ai`, with the same API key, the same models and the same request format. The difference is which flock is tried first.

## Call it

Use the address as your base URL:

```bash
curl https://flockadoo-flock1.flock.flockadoo.ai/v1/chat/completions \
  -H "Authorization: Bearer $FLOCKADOO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "Qwen/Qwen2.5-7B-Instruct", "messages": [{"role": "user", "content": "Hello"}]}'
```

In an OpenAI client, set the base URL to `https://flockadoo-flock1.flock.flockadoo.ai/v1`.

## Which flock serves you

| The provider's flock | What happens |
|---|---|
| Can serve the model, within your max price | It is tried first. |
| Is busy, offline, paused, over your max price, or does not have the model | Your call goes to the marketplace, as on `core.flockadoo.ai`. |
| The address points at no flock | Your call goes to the marketplace. |

Your [max price limits](max-price-limits.md), [monthly spending caps](monthly-spending-caps.md) and [routing options](request-routing-options.md) apply as usual. An address never stops a call that `core.flockadoo.ai` would serve.

`/v1/models` on an address lists every model, because the marketplace can serve any of them.

## What you pay

The same as through `core.flockadoo.ai`: the price set by the flock that served your call. The address changes how Flockadoo and the provider split the fee, not what you pay.

## Related

- [Using the API](using-the-api.md)
- [Max price limits](max-price-limits.md)
- [Flock addresses, for providers](../provider/flock-addresses.md)
