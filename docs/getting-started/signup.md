# Sign up and create a cluster

Create an Inferoute account, deploy a provider cluster, and copy the **provider API key**. You need that key for [Installation](installation.md).

## Sign up

1. Open [www.inferoute.com](https://www.inferoute.com).
2. Click **Connect your GPUs** (on a phone, **Connect GPUs**).
3. On **Sign Up**, enter your email and click **Continue**, or choose **GOOGLE** or **GITHUB**.
4. Open the **Complete your Inferoute signup** email. The link expires in **24 hours**. On **Choose a password**, set a password of at least **8** characters and click **Sign up**. You land in the dashboard.

## Choose Provider

On first login you see **Welcome Onboard!** and **Please, choose your role:**

- **Provider** — earn by offering GPU inference
- **Consumer** — call models as a buyer
- **I want both** — if you will do both

Choose **Provider** (or **I want both**). Switch between **Provider** and **Consumer** later with the control in the top bar.

Two-factor authentication, sessions, and password changes live under **Account settings** → **Sign-in & security**. A login lasts **24 hours**. See [Sign-in and security](../account-security.md).

## Deploy a cluster

1. Open **Clusters** (under **Operate**).
2. Click **Deploy a cluster**.

The wizard has two steps.

### 1. Check compatibility

Set **Cluster type**:

- **Single node** — one machine.
- **Multi-node** — this key is the master. Share the cluster page so workers can request an invite. When the slots are filled, start the master first. Workers then have 60 minutes to join. See [Multi-node clusters](../provider/multi-node-clusters.md).

If you pick **Multi-node**, those machines share a private network. Only create or join one with people you intend to share GPUs with. Read [Multi-node networking](../provider/multi-node-networking.md) before you create a key or accept a join.

Then set **Operating system**. The page lists what that machine needs. You do not install the engine in this step. Setup installs it later if it is missing.

- **Linux:** vLLM. You need an NVIDIA GPU.
- **macOS:** vLLM Metal. Apple Silicon only. Intel Macs are not supported. The client [setup wizard](../provider-client/setup.md) on a Mac also offers llama.cpp. See [Setup: macOS](../provider-client/setup-mac.md).
- **Windows:** llama.cpp. It does not serve every catalog model. Encoder and embedding models such as `baai/bge-m3` stay off Windows.

Click **Next step**.

### 2. Create a key and install the client

1. Set **Cluster name**. For example, `inferoute-cluster1`.
2. Set **Key name**. It defaults to `{cluster name} API key`.
3. Click **Create key**.
4. Click **Copy**. The page says the key is shown once.

The install command is filled in. Copy it, or follow [Installation](installation.md) and substitute the key yourself. Click **Done, go to clusters** when you are finished.

You set model prices **after** the client is running, on the cluster **Models** tab — see [Model pricing](../provider/model-pricing.md). Native Windows uses **llama.cpp**, not vLLM.

On a multi-node cluster, run that command on the master first. Then set the intended model and minimum VRAM on the cluster **Settings** tab, and add workers from **Nodes**.

## Copy the key later from Settings

If you already have a cluster and need the key again:

1. Open **Clusters** and select the cluster (for example **inferoute-cluster1**).
2. Open **Settings**.

Under **Client API key**, click **Create a key** if the cluster has none, or **Replace key** for an existing key. Replacing the key stops the old secret immediately. Copy the new secret from **Copy the new key** and restart the client before you expect inference to work.

The full secret is only shown when you create or replace it. Settings otherwise shows a masked suffix.

More on keys, pause, and delete: [Deleting and managing clusters](../provider/deleting-clusters.md). To add workers and split earnings, see [Inviting nodes](../provider/inviting-nodes.md) and [Cluster earnings](../provider/cluster-earnings.md).

## Next

Install the client with that key: [Installation](installation.md).
