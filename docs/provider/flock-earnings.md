# Flock earnings

Buyers pay for inference. After Flockadoo’s fee, the rest is the flock payout. A **single-node** flock credits that whole payout to you.

A **Team Flock** flock can split it. You set a **commission** on the **Nodes** tab. That percent comes off first. What remains is split evenly across the **master** (you) and every worker marked **In the flock**.

## Set the commission

1. Open **My Flocks** under **Inference**.
2. Select the Team Flock.
3. Open **Nodes**.
4. Under **Commission**, enter a percent from 0 to 100.
5. Click **Save commission**.

People see this percent on the flock page (**Explore** → **GPU flocks**, then the flock) before they request an invite.

If you never save a commission, or no worker is **In the flock** yet, you keep the whole payout.

Machines marked **Waiting to join** are not in the split. Only workers marked **In the flock** are.

## Example

For example, a payout of **$100** on **flockadoo-flock1**, with commission **10%** and **two** active workers:

| Who | Share |
| --- | --- |
| Commission (you) | $10 |
| Remainder | $90, split 3 ways (you + 2 workers) |
| You, total | $40 |
| Each worker | $30 |

The Nodes page states the same rule: at 10% with two workers, you get the 10% plus one third of what remains.

At **100%** you keep the payout and workers get nothing. At **0%** the whole payout is split evenly, with no commission taken off first.

## Where it shows up

The share is added to each person’s balance. Open **My Flocks**, then the **Earnings** tab. **Your balance** is that account balance (the same number **Withdraw** uses). **Earned today** on that page is income from flocks you **own**, and it is the flock total before the split. A worker who does not own a flock will not see their join income in **Earned today** there. It is still in **Your balance**.

Open the flock from **My Flocks** for the per-flock **Earnings** tab:

| Who is looking | **Earned today** and **Total earnings** on that flock |
| --- | --- |
| You (the owner) | The flock total, before commission and the worker split |
| A worker | That person’s share only |

A worker does not get their own flock, a provider API key, or the **Nodes** and **Settings** tabs. They can open **Earnings**, **GPUs**, and **Models**. **Models** is read-only for them.

Changing commission affects **later** payouts. It does not rewrite payouts already credited.

Prices buyers pay are still the prices on the flock **Models** tab. Commission does not change those prices. See [Model pricing](model-pricing.md).

## Related

- [Team Flocks](team-flocks.md)
- [Inviting nodes](inviting-nodes.md)
- [Joining a flock](joining-a-flock.md)
