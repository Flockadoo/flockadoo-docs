# Setup: macOS (Apple GPU)

Use this guide when you run the provider client natively on a Mac with Apple Silicon. For example, **flockadoo-cluster1** on a MacBook. You need **48 GB** of unified memory to run approved vLLM Metal models (BF16 7B-class). Intel Macs are not supported.

## Quick install (recommended)

1. Get your provider API key — see [Sign up and create a cluster](../getting-started/signup.md).
2. Run the install script:

   ```bash
   curl -fsSL https://raw.githubusercontent.com/flockadoo/flockadoo/main/scripts/install.sh | bash
   ```

The [setup wizard](setup.md) offers **vLLM Metal** or **llama.cpp**. It installs the one you pick if it is missing, offers to replace a vLLM Metal release older than **0.30.0** (see [Supported engine versions](setup.md#supported-engine-versions)), and shows which models fit this Mac. vLLM Metal serves on `http://127.0.0.1:8000`. llama.cpp installs into `~/.local/share/flockadoo/llama.cpp` and serves on `http://127.0.0.1:8081`. Re-run anytime:

```bash
flockadoo setup
```

The script places **flockadoo** in `/usr/local/bin`.

3. Start the client:

   ```bash
   flockadoo
   ```

Default config: `~/.config/flockadoo/config.yaml`. Logs: `~/.local/state/flockadoo/log`.

## Apple GPU monitoring

On macOS the client reports basic GPU information (model name and core count). It does **not** report GPU memory or utilization, so load from other processes does not set the health-report busy flag. A request in flight still does (default one at a time). See [How it works](how-it-works.md).

On Linux with NVIDIA, the health report also marks the GPU busy when utilization is above **20%**. See [Setup: Linux](setup-linux.md).

## Manual install from source

1. **Go:** Install Go 1.22 or higher.
2. **Clone and build:**

   ```bash
   git clone https://github.com/flockadoo/flockadoo.git
   cd flockadoo
   go build -o flockadoo ./cmd
   ```

3. Run **`flockadoo setup`**, then:

   ```bash
   ./flockadoo --config ~/.config/flockadoo/config.yaml
   ```

The client opens an outbound connection to Flockadoo — no ngrok or open firewall ports required.

## Related

- [Setup wizard](setup.md)
- [Installation](../getting-started/installation.md)
- [Configuration](configuration.md)
- [Setup: Linux](setup-linux.md)
- [Setup: Windows](setup-windows.md)
- [FAQ](faq.md)
