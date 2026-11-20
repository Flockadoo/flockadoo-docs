# Flock location

The dashboard shows a **country flag** next to each flock on **My Flocks** so you can see where your GPU is running at a glance.

## What you see

On **My Flocks**, each row shows:

- Flock name
- **Country flag** (when location is known)
- GPU count and other status

If location is not available yet, you see **—** instead of a flag. That usually means the client has not connected yet.

## How location is determined

You do **not** configure location in the client or dashboard.

Flockadoo detects location automatically from the connection your provider client opens:

1. Your provider client connects to Flockadoo.
2. Flockadoo reads the public IP of that connection.
3. The platform resolves that IP to a **country code** and stores it on your flock.

Location updates when:

- The flock first connects
- The client reconnects from a different network (for example after you move the machine)

## What you need to do

Nothing extra. Keep the provider client running, as described in [How it works](../provider-client/how-it-works.md).

## Related

- [Deleting and managing flocks](deleting-flocks.md)
- [Flock location](flock-location.md)
- [Provider client: connection](../provider-client/how-it-works.md#connection-to-flockadoo)
