# Model pricing

Each **flock** has its own model list and prices. Changing prices on one flock does **not** change prices on your other flocks, even when they run the same model name.

For example, if **flockadoo-flock1** and **flockadoo-flock2** both serve `Qwen/Qwen2.5-7B-Instruct`, you can set different input and output prices on each flock. Buyers see the price for the flock that actually runs their request.

## Where to edit prices

1. Open **My Flocks** in the dashboard.
2. Select a flock (for example **flockadoo-flock1**).
3. Open the **Models** tab.
4. Edit **Input / 1M** and **Output / 1M**.
5. Click **Save** on that row.

New models start at the market-average price. You can change a model's price once it shows **Verified**, whether or not it shows **Serving** right now. A model that shows **Not verified** keeps the market-average price and can't be repriced.

| Verification | Serving | Gets traffic | Can reprice |
|---|---|---|---|
| Verified | Serving | Yes | Yes |
| Verified | Not serving | No | Yes |
| Not verified | Not serving | No | No |

Each model has a maximum price. Saving above it returns an error that states the maximum. Prices are in $/1M with up to 2 decimals.

**Apply market averages to all** fills only the rows you can edit. It does not save automatically. If your prices differ a lot from the market average, you may see a confirmation before saving a single row.

## Pricing is per flock, not global

| What you do | Effect |
|-------------|--------|
| Change prices on **flockadoo-flock1** | Only that flock’s listed prices change |
| Same model name on **flockadoo-flock2** | Unchanged unless you edit that flock too |
| **Models & Prices** (account-wide tab) | Read-only overview across flocks — not where you edit |

Use the flock **Models** tab when you want different prices per machine, region, or GPU tier. Set the same numbers on each flock if you want uniform pricing everywhere.

## Units in the dashboard

All editable prices in the flock **Models** tab are **per 1 million tokens** ($/1M):

- **Input / 1M** — prompt / input tokens  
- **Output / 1M** — completion / output tokens  

That matches how **Models & Prices** displays prices elsewhere in the dashboard.

## Deploy wizard

When you deploy a new flock, the client starts models at the market-average price. After a model shows **Verified**, change its price on that flock’s **Models** tab.

## Provider API (automation)

If you automate with a **provider API key**, prices are still **per flock** (one key per flock). Call the platform at `https://core.flockadoo.ai` — not the [local REST API](../provider-client/rest-api.md) on the machine.

Authenticate with `Authorization: Bearer <provider API key>`. Prices are $/1M, the same numbers as the dashboard. Get `model_id` from `GET /api/provider/models`.

`PATCH /api/provider/models/{model_id}/pricing`

Both fields are required JSON numbers. `0` is allowed. At most 2 decimal places. No exponent. No other fields.

| Code | When |
|---|---|
| 400 | Bad number, unknown field, more than 2 decimals, or above the model's maximum |
| 404 | That model is not on this flock |
| 409 | `model_not_verified` — the model is still on the market-average price |

For example, $0.15 input and $0.60 output:

```bash
curl -X PATCH "https://core.flockadoo.ai/api/provider/models/{model_id}/pricing" \
  -H "Authorization: Bearer YOUR_PROVIDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input_price_per_1m": 0.15,
    "output_price_per_1m": 0.60
  }'
```

Changing the price on **flockadoo-flock1** does not change **flockadoo-flock2**.

## Related

- [Deleting and managing flocks](deleting-flocks.md)
- [Provider client FAQ](../provider-client/faq.md)
