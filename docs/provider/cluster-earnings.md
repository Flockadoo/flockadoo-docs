# Cluster earnings

Buyers pay for inference. After Inferoute’s fee, the rest is the cluster payout. A **single-node** cluster credits that whole payout to you.

A **multi-node** cluster can split it. You set a **commission** on **Settings**. That percent comes off first. What remains is split evenly across the **master** (you) and every worker who has finished setup.

## Set the commission

1. Open **Clusters** (under **Operate**).
2. Select the multi-node cluster.
3. Open **Settings**.
4. Under **Multi-node only**, find **Commission**.
5. Set a percent from 0 to 100 and click **Save commission**.

People see this percent on the cluster page (**Explore** → **GPU clusters**, then the cluster) before they request an invite.

If you never save a commission, or no worker has finished setup yet, you keep the whole payout.

A machine marked **Waiting to join** is not in the split. It joins the split once that chip is gone and the row shows **Healthy** or **Unhealthy**.

## Example

For example, a payout of **$100** on **inferoute-cluster1**, with commission **10%** and **two** active workers:

| Who | Share |
| --- | --- |
| Commission (you) | $10 |
| Remainder | $90, split 3 ways (you + 2 workers) |
| You, total | $40 |
| Each worker | $30 |

**Nodes** states the same rule: at 10% with two workers, you get the 10% plus one third of what remains. Change the percent on **Settings**. **Nodes** shows the split.

At **100%** you keep the payout and workers get nothing. At **0%** the whole payout is split evenly, with no commission taken off first.

## Where it shows up

The share is added to each person’s balance. Open **Clusters**, then the **Earnings** tab. **Balance** is that account balance. **Payout settings** opens **Account settings** → **Payouts**. Payouts are not live yet, so nothing on that page is saved. **Earned today** on the **Balance** card is income from clusters you **own**, and it is the cluster total before the split. A worker who does not own a cluster will not see their join income in **Earned today** there. It is still in **Balance**. The chart on that page does include a worker’s own share.

The period control is **7D** (last 7 days), **30D** (last 30 days), or **1Y** (last 12 months).

Open the cluster for its own **Earnings** tab. The period control there is **7D**, **30D**, or **90D** (last 13 weeks).

| Who is looking | What **Earned** shows |
| --- | --- |
| You (the owner) | The cluster payout after the platform fee, before commission and the worker split. The heading is **Earned**. |
| A worker | That person’s share only. The heading is **Your share**. |

A worker does not get their own cluster, a provider API key, or the **Nodes** and **Settings** tabs. They can open **Earnings**, **GPUs**, and **Models**. **Models** is read-only for them.

Changing commission affects **later** payouts. It does not rewrite payouts already credited.

Prices buyers pay are still the prices on the cluster **Models** tab. Commission does not change those prices. See [Model pricing](model-pricing.md).

## Related

- [Multi-node clusters](multi-node-clusters.md)
- [Inviting nodes](inviting-nodes.md)
- [Joining a cluster](joining-a-cluster.md)
