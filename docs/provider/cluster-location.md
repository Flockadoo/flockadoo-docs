# Cluster location

The dashboard shows a **country code** on each cluster under **Clusters** so you can see where the machine is connecting from.

## What you see

On **All clusters**, each card shows a two-letter code when location is known. For example, `US`. The cluster page shows the same code next to the name. **Hardware** lists **Location** from the same detection.

If location is not available yet, the card shows **··** instead of a code. That usually means the client has not connected yet.

## How location is determined

You do not configure location in the client or dashboard.

Inferoute detects location automatically from the connection your provider client opens:

1. Your provider client connects to Inferoute.
2. Inferoute reads the public IP of that connection.
3. The platform resolves that IP to a country code and stores it on your cluster.

Location updates when:

- The cluster first connects
- The client reconnects from a different network (for example after you move the machine)

## What you need to do

Nothing extra. Keep the provider client running, as described in [How it works](../provider-client/how-it-works.md).

## Related

- [Deleting and managing clusters](deleting-clusters.md)
- [Provider client: connection](../provider-client/how-it-works.md#connection-to-inferoute)
