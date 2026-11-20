# Using your own flocks

If you run Flockadoo flocks on the same account you use for API requests, your flocks join the normal provider pool for your requests. You don't need to turn anything on.

## How your flocks are billed

Requests served by your own flocks are billed at **$0**. You pay no token cost and no platform service fee, and your flock earns nothing for them. Flockadoo still records the usage.

## How your flocks are picked

Flockadoo ranks your flocks alongside marketplace providers, using each flock's **listed price** and speed. Your flocks are not tried first.

| Rule | Marketplace providers | Your own flocks |
|---|---|---|
| **Max price** (profile, key, and request) | Applies | Does not apply |
| `min_tokens_per_second` | Applies | Applies |
| Must be healthy, verified, and connected | Yes | Yes |

For example, say you list `Qwen/Qwen2.5-7B-Instruct` on **flockadoo-flock1** at $2.00 per 1M output tokens, and your max price is $1.00 per 1M. **flockadoo-flock1** still qualifies for your requests, because max price doesn't apply to your own flocks. It is ranked by its $2.00 listed price, though, so a cheaper marketplace provider may be picked first.

!!! info

    There is no setting that forces your requests onto your own flocks. To make your flock more likely to win, list it at a lower price on the **Models** tab.

## Related

- [Using the API](using-the-api.md)
- [Max price limits](max-price-limits.md)
- [Request routing options](request-routing-options.md)
- [Model pricing](../provider/model-pricing.md)
