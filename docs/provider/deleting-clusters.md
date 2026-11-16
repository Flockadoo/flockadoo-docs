# Deleting and managing clusters

This page covers **dashboard** actions for a provider cluster: status, the API key, pause and resume, and removal. To create a cluster and copy a key, see [Sign up and create a cluster](../getting-started/signup.md). For installing the client, see [Installation](../getting-started/installation.md).

## Where to find a cluster

1. Switch the top bar to **Provider**.
2. Open **Clusters** (under **Operate**).
3. Stay on **All clusters** and select the cluster. For example, **inferoute-cluster1**.

**Settings** holds the client API key, removal, and (on a multi-node cluster) the intended model, VRAM, vLLM version, and commission. Pause and resume are on the cluster page itself, not on **Settings**.

## Status

Health and pause are separate. You can be **Healthy** and **Paused** at the same time.

| What you see | Meaning |
| --- | --- |
| **Healthy** | The client is reporting in |
| **Unhealthy** | A report is missing, or a node is down |
| **Paused** | You turned new requests off. The client can keep reporting |

On **All clusters**, filter with **All**, **Healthy**, **Unhealthy**, and **Paused**. **Paused** can sit on top of a health filter. Sort with **Earned · 7d**, **Name**, or **Status**.

A card shows a country code (for example `US`) when location is known. See [Cluster location](cluster-location.md).

If the client stops reporting, the cluster turns **Unhealthy** after about 5 minutes, paused or not. Pause does not freeze the last green status. A paused cluster does not send a **Cluster outage** email. A running one can. See [Email notifications](../email-notifications.md).

An **Unhealthy** card that is still running names the last heartbeat and tells you to check the machine and its engine.

## Uptime

**Overview** shows **Uptime · this week**. Each day is the share of health reports that were healthy.

Time the client is offline counts as down, once the cluster has been healthy at least once. Time before that first healthy report does not. Time you spend paused does not.

## Hardware

**Overview** → **Hardware** lists GPU, VRAM per node, Engine, Driver, CUDA, and Location. Open **GPUs** for the live readings.

**GPUs** shows **Total VRAM**, **Engine**, temperature, power draw, and utilization for **24H** or **7D**.

The client reports one GPU. **Total VRAM** multiplies that reading by the GPU count. On a machine with more than one GPU, the live meters are from GPU 0. Apple Silicon shows **Unified memory (GPU limit)** and is not multiplied.

A missing sensor shows **—**. Power marked **est.** is a scale we draw when the GPU does not report a limit, such as Apple Silicon. High VRAM use is normal: vLLM reserves most of the memory for its cache. Readings come from each node's heartbeat every few minutes.

## API keys

Each cluster has one **provider API key**. The client on your machine uses it to connect.

On **Settings**, under **Client API key**, you can:

- See the key name, a masked suffix (`ifr_••••` plus the last characters), and **In use**.
- Click **Replace key**, then confirm **Replace key**. The old secret stops immediately. **Copy the new key** shows the secret once. Restart the client with it, or the machine stops connecting. On a multi-node cluster, copy the start command again on **Nodes** and restart the client on every node.
- Click **Create a key** if the cluster has none.

Replacing or creating a key does not remove the cluster.

## Pause and resume

On the cluster page, **Pause cluster** stops new inference from being routed to the cluster. The client can keep running. **Resume cluster** turns routing back on, subject to health.

On **All clusters**, the card buttons are **Pause** and **Resume**. They do the same thing.

Use pause when you want to go idle without removing the cluster.

If **Cluster paused** email is on, you can get an email with a link to that cluster. See [Email notifications](../email-notifications.md).

## Remove cluster

**Remove cluster** is at the bottom of **Settings**. The button is **Remove** followed by the cluster name. Confirm **Remove cluster**.

Use it when you want the cluster off your account and inference stopped.

### What happens when you remove it

1. **The cluster leaves your dashboard.** It no longer appears under **Clusters**.
2. **Inference stops.** The cluster is paused, marked unavailable, and health is set to red, so Inferoute will not route requests to it.
3. **The API key is revoked.** The provider client can no longer authenticate with it.
4. **Earnings so far stay** in your balance and history.
5. **A multi-node machine leaves the private network.** Stop the client on that machine too. See [Multi-node networking](multi-node-networking.md).

### What removal does not do

- It does not uninstall the provider client. Stop it on the machine if you no longer need it.
- It does not delete your Inferoute account or your other clusters.

### After removal

You cannot pause, resume, view earnings for, or create a new API key on a removed cluster. To offer inference again, click **Deploy a cluster**.

Removal is not reversible from the dashboard. If you removed a cluster by mistake, contact support.

## Pause vs remove

| | Pause | Remove |
| --- | --- | --- |
| Stops new inference | Yes | Yes |
| Cluster stays in the dashboard | Yes | No |
| API key keeps working | Yes | No (revoked) |
| Reversible from the cluster page | Yes (**Resume cluster**) | No |
| Earnings history | Kept | Kept |

## Related

- [Sign up and create a cluster](../getting-started/signup.md)
- [Installation](../getting-started/installation.md)
- [Email notifications](../email-notifications.md)
- [Cluster location](cluster-location.md)
- [Model pricing](model-pricing.md)
- [Multi-node clusters](multi-node-clusters.md)
- [Multi-node networking](multi-node-networking.md)
- [Provider client introduction](../provider-client/introduction.md)
