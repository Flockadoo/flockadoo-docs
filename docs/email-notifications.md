# Email notifications

You can choose which emails Flockadoo sends you. Preferences live in **Account Settings** and apply to the email on your account.

## Where to manage them

1. Open the dashboard and go to **Account Settings** (from the user menu).
2. Open the **Notifications** tab.
3. Turn each notification type **on** or **off**. Changes save as soon as you toggle them (except **Low Balance Warning**, which also needs a threshold — see below).

Emails go to the address shown on that page (your account email). The address must be **verified** for notification emails to be delivered.

## Notification types

| Type | What you get | Who it is for |
| --- | --- | --- |
| **Platform updates** | Product news, features, and announcements | Everyone who opts in |
| **Low balance warning** | An email when your account balance drops below an amount you choose | Anyone spending from a wallet balance |
| **Flock paused** | An email when one of your GPU flocks is paused | Providers |
| **Flock outage** | An email when a flock is no longer healthy or available | Providers |

Turn **Platform updates** off if you only want operational alerts (or turn everything off if you prefer no email).

## Low balance

When **Low Balance Warning** is on, we check your available wallet balance about once an hour. If it is below the threshold you set, we email you so you can top up before requests start failing.

1. Turn **Low Balance Warning** on.
2. Enter an amount between **$1** and **$1000**.
3. Click **Save**.

Until you save a threshold, we do not send low balance emails for your account.

This is separate from [monthly spending caps](consumer/monthly-spending-caps.md). Caps limit spend on a single API key; a low balance means the account wallet itself is low.

## Flock paused

If you (or someone with access) **pauses** a flock in the dashboard, we can email you. The message includes a link to that flock’s page under **My Flocks** so you can resume or check settings.

Pausing stops new inference from being routed to the flock. See [Deleting and managing flocks](provider/deleting-flocks.md).

## Flock outage

If a flock stops reporting as healthy (for example it goes offline or misses health checks) while it is **not** paused, we can email you. The email links straight to that flock in the dashboard.

This is meant for flocks that should be running but are no longer available to receive work. A paused flock does not trigger an outage email.

## Flock join

Join mail is separate from the toggles above. You cannot turn it off on **Notifications**. It is sent only when a join actually happens, and only to a **verified** account email. The join code is never in the email.

| When | Who is emailed |
| --- | --- |
| Someone clicks **Request invite** | The flock owner and the person who asked |
| The owner clicks **Accept** or **Reject** | The person who asked |
| The owner clicks **New code**, **Revoke**, or **Remove** | The person who asked or the worker who was removed |

The owner’s email links to that flock’s **Nodes** tab and includes the requester’s preferred contact (account email, Telegram, or Discord). The requester’s accept email tells them to open the flock page and use **Show join code**. That code is shown once on that page.

See [Inviting nodes](provider/inviting-nodes.md) and [Joining a flock](provider/joining-a-flock.md).

## Things to keep in mind

- **Toggles are per account.** Preferences apply to your user, not per API key or per flock.
- **Verified email only.** If your email is not verified, notification emails will not be sent until you verify it.
- **Operational alerts can be quiet.** We avoid spamming the same alert repeatedly; you may not get another email for the same issue until the situation clears and happens again (or, for some flock alerts, until some time has passed).
- **Platform updates are optional.** They are off by default. Turn them on only if you want product and announcement mail.

## Related

- [Deleting and managing flocks](provider/deleting-flocks.md) — pause, resume, and delete
- [Inviting nodes](provider/inviting-nodes.md) — accept or reject a join request
- [Monthly spending caps](consumer/monthly-spending-caps.md) — per-key spend limits
- [Overview](index.md)
