# Flock addresses

A flock address is your own API endpoint, such as `flockadoo-flock1.flock.flockadoo.ai`. Give it to your customers. Calls that come in through it try your flock first, and you pay a lower fee on the calls your flock serves. If your flock is busy, the call goes to another flock, and you still earn a share of the fee for bringing the customer.

## What it costs

| | |
|---|---|
| Price | **$5**, once, from your wallet. No renewal. |
| Wallet | You need at least **$10** in your wallet to buy one. |
| Limit | Five addresses per account. |
| Who can buy | Any account. You do not need a flock to buy or keep one. |

The rates and prices can change. The **My Addresses** page and the homepage always show the ones in force.

## Buy an address

1. Open **My Addresses** in the dashboard, under **My Flocks**.
2. In the **New address** bar at the bottom, type a name. A name is 3 to 32 characters: lowercase letters, digits and hyphens, starting and ending with a letter or digit.
3. Click **Buy for $5**.
4. Check the address and the price, and click **Buy** again to confirm.

The price comes out of your wallet straight away. Some names are reserved, such as `www`, `docs` and well-known brand names. A name someone else owns cannot be bought.

## Point it at a flock

Each address points at one of your flocks, or at none.

1. Open **My Addresses**.
2. In the address's row, click the button under **Flock**. It says **No flock** until you choose one.
3. Pick a flock from the list. A flock that is unhealthy or paused is marked.

To move the address, choose another flock. To stop using a flock, choose **No flock**. An address with no flock still works: its calls run through the Flockadoo marketplace, and you still earn your share of the fee.

The line under the flock says who is serving the address's calls right now: your flock, at the lower fee, or other flocks, when yours is unhealthy or paused or there is none.

If you delete a flock, its addresses are set to **No flock**. The addresses stay yours.

## What you earn

For example, a customer spends **$100** through `flockadoo-flock1.flock.flockadoo.ai`:

| Who serves the call | The flock that served | You, as the address owner | Flockadoo |
|---|---|---|---|
| Your own flock (any of them) | $98 (you) | | $2 |
| Another flock | $95 (that flock) | $1 | $4 |
| A call through `core.flockadoo.ai`, for comparison | $95 | | $5 |

The fees come off the provider's side. The customer pays the price the serving flock set.

Calls you make yourself through your own address are not counted. Calls on your own flock cost you nothing, as always.

The **My Addresses** page shows, for each address, the requests that came through it, how many customers made them, what they spent, and what you earned.

## An address is permanent

An address is yours for good. It cannot be deleted or renamed, and there is no renewal. You can point it at a different flock at any time.

## Related

- [Using a flock address](../consumer/flock-addresses.md)
- [Flock earnings](flock-earnings.md)
- [Model pricing](model-pricing.md)
