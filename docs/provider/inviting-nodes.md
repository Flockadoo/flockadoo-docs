# Inviting nodes

You invite workers to a Team Flock you own. They ask to join. You accept or reject. Accepting creates a **join code** they paste into setup. For what a master and a worker are, see [Team Flocks](team-flocks.md).

## Create the flock

1. Open **My Flocks** under **Inference**.
2. Click **Deploy a Flock**.
3. On **Check Compatibility**, set **Flock type** to **Team Flock**.
4. Finish the wizard and copy the provider API key. That key is the **master**. It is shown once.

Run `flockadoo setup` on your machine with that key. The prompt is **Provider API key or join code**. Setup sees a Team Flock and installs this machine as the master. It uses the **intended model** you saved on **Nodes**. If no model is saved, setup stops with `flock … has no model set. Choose one in the dashboard, then re-run setup`.

Setup downloads **winglink** and may ask for your password (`winglink needs root to create winglink0`). It prints the vLLM command and does not start the engine. See [How the machines connect](team-flocks.md#how-the-machines-connect).

## Review a request

When someone asks to join, you get an email (if their account email is verified). The email does **not** contain a join code. It names them and their preferred contact, and links to the **Nodes** tab.

1. Open the flock.
2. Open **Nodes**.
3. Under **Join requests**, read the username and how to reach them (email, Telegram, or Discord).
4. Click **Accept** or **Reject**.

**Accept** shows a join code once, on that page:

`join-` followed by a long hex string.

Copy it before you leave. Flockadoo does not show it again, and it is not emailed. You can also send it yourself using the contact on the request. The person who asked can open the same code once on the flock page. See [Joining a flock](joining-a-flock.md).

**Reject** declines the request. They can ask again.

They can **Cancel request** while it is still pending. Then it disappears from **Join requests**.

## After they join

**Nodes** lists each machine: role (**Master** or **Worker**), whether they are in the flock, and health. A worker shows up there after setup uses the code. Before that, they stay under **Invited**.

The join code works **once**. After setup uses it, that code cannot be used again.

When enough machines are in, start the master first. Once it is up, tell the workers. They have **60 minutes** to join. See [Start the master first](team-flocks.md#start-the-master-first). Copy the flock link on **Nodes** and send that page before they request an invite, so they can read the model, the GPU on the master, and the VRAM first. Same GPU on every machine is what Flockadoo tests. See [GPUs across nodes](team-flocks.md#gpus-across-nodes).

**Invited** lists people you accepted who have not finished setup. It shows the same contact as the request. It does not show the code.

If they lose the code before setup, click **New code**. That kills the old code and shows a new one once, on that page. They can also open it once on the flock page. Flockadoo emails them to look there. The code is not in the email.

**Revoke** withdraws an invite that has not been used. They can **Request invite** again.

## Remove a worker

On a machine that already joined, **Remove** takes that worker out of the flock. Their machine can no longer serve it, and they stop earning from it. They can ask to join again. You cannot remove the master from this list. Deleting the flock is still how you shut the whole thing down.

## Related

- [Joining a flock](joining-a-flock.md)
- [Flock earnings](flock-earnings.md)
- [Setup wizard](../provider-client/setup.md)
- [Email notifications](../email-notifications.md)
