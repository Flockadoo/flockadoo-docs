# Deleting and managing flocks

This page covers **dashboard** actions for a provider flock: API keys, pause/resume, and deletion. To create a flock and copy a key, see [Sign up and create a flock](../getting-started/signup.md). For installing the client, see [Installation](../getting-started/installation.md).

## Where to find flock settings

1. Open **My Flocks** in the dashboard.
2. Select the flock you want to manage.
3. Go to the **Settings** tab.

Settings replaces the old **Actions** tab. API key management, pause/resume, and delete all live here.

## API keys

Each flock has one or more **provider API keys**. The client on your machine uses this key to authenticate with Flockadoo.

On Settings you can:

- **View** the key label and a masked suffix (last characters of the lookup key).
- **Re-Generate Key** — the old secret stops working immediately; copy the new key into your client config.
- **Create API Key** if the flock has none (for example after all keys were revoked).

The full API key is only shown **once** when it is created or re-generated. Store it somewhere safe before closing the modal.

Re-generating or creating a key does **not** delete the flock. It only rotates credentials for that flock.

## Pause and resume

On Settings, under **Pause Inference**:

**Pause Flock** stops new inference orders from being routed to your flock. Your provider client can keep running, but Flockadoo will not send new work while the flock is paused.

**Resume Flock** turns routing back on (subject to health and availability checks).

The flock list uses the same actions as **Pause flock** / **Resume flock**.

Use pause when you want to go idle temporarily without removing the flock from your account.

If email notifications for **Flock paused** are enabled, you can get an email when a flock is paused, with a link to that flock. See [Email notifications](../email-notifications.md).

## Delete flock

**Delete flock** is in the **Danger zone** on Settings. It is meant when you want to remove a flock from your account and stop inference immediately.

### What happens when you delete

When you confirm deletion:

1. **The flock is removed from your dashboard** — it no longer appears under **My Flocks**.
2. **Inference stops** — the flock is paused, marked unavailable, and health is set to red so Flockadoo will not route requests to it.
3. **All active API keys for that flock are revoked** — your provider client can no longer authenticate with those keys.
4. **Historical data is kept** — past earnings and transactions stay in your account history for billing and audit. The flock no longer appears in the dashboard, but we retain records tied to past payouts.
5. **A Team Flock machine leaves the private network** — deleting the flock, or leaving it, drops that machine from the network the flock used. Stop the client on the machine too. See [Team Flock networking](Team Flock-networking.md).

### What delete does not do

- It does **not** uninstall the provider client on your machine — stop the service locally if you no longer need it.
- Stop the client on that machine so it closes its connection and no longer accepts traffic.
- It does **not** delete your Flockadoo user account or other flocks.

### After deletion

You **cannot** pause, resume, view earnings for, or create new API keys against a deleted flock. To offer inference again, deploy a **new** flock (for example via **Deploy a flock**).

Deletion is **not reversible** from the dashboard today. If you deleted a flock by mistake, contact support.

## Pause vs delete

| | Pause | Delete |
| --- | --- | --- |
| Stops new inference | Yes | Yes |
| Flock stays in dashboard | Yes | No |
| API keys keep working | Yes | No (revoked) |
| Reversible from Settings | Yes (resume) | No |
| Earnings history | Kept | Kept |

Use **pause** for temporary downtime. Use **delete** when you are done with that flock for good.

## Related

- [Sign up and create a flock](../getting-started/signup.md)
- [Installation](../getting-started/installation.md)
- [Email notifications](../email-notifications.md)
- [Flock location](flock-location.md)
- [Model pricing](model-pricing.md)
- [Team Flocks](team-flocks.md)
- [Team Flock networking](Team Flock-networking.md)
- [Provider client introduction](../provider-client/introduction.md)
