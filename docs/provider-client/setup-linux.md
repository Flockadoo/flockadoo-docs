# Setup: Linux (NVIDIA)

Use this guide when you run the provider client natively on Linux with an NVIDIA GPU. For example, **flockadoo-flock1** on a workstation. You need at least **32 GB** of system memory and **24 GB** of VRAM for approved vLLM models.

## Quick install (recommended)

1. Get your provider API key — see [Sign up and create a flock](../getting-started/signup.md).
2. Run the install script:

   ```bash
   curl -fsSL https://raw.githubusercontent.com/flockadoo/flockadoo/main/scripts/install.sh | bash
   ```

The [setup wizard](setup.md) installs **vLLM** if it is missing, offers to replace a release older than **0.30.0** (see [Supported engine versions](setup.md#supported-engine-versions)), and shows which models fit this GPU. Re-run anytime:

```bash
flockadoo setup
```

3. Start the client:

   ```bash
   flockadoo
   ```

Default config: `~/.config/flockadoo/config.yaml`. Logs: `~/.local/state/flockadoo/log`.

## NVIDIA GPU

- At least **32 GB** of system memory.
- At least **24 GB** of VRAM (for example RTX 3090 or RTX 4090).
- Install the [NVIDIA driver](https://www.nvidia.com/drivers) so `nvidia-smi` is on `PATH`. The wizard will not offer vLLM if `nvidia-smi` is missing.
- The client uses `nvidia-smi` for GPU name, VRAM, and utilization in the health report. Utilization above **20%** sets the GPU busy flag in that report. A new request is rejected when an inference slot is full. See [How it works](how-it-works.md).
- The install script does not install the driver.

## Blackwell GPUs

vLLM on a GPU with compute capability **10.0** or higher also needs FlashInfer kernels. That includes datacenter Blackwell and RTX 50-series. Hopper (**9.0**), Ada, and Ampere (for example an RTX 3090 or RTX 4090) skip this step.

When the wizard installs vLLM, it reads compute capability from `nvidia-smi`. At **10.0** or higher it prints **Blackwell GPU detected. Downloading FlashInfer kernels...** and downloads the kernels before setup continues. If that download fails, setup stops with **vLLM kernel download failed**.

If `nvidia-smi` cannot report compute capability, setup prints **Skipping vLLM kernel download** and continues. On a Blackwell GPU, vLLM can then fail to start. Fix `nvidia-smi`, then run `flockadoo setup` again.

Check the value yourself:

```bash
nvidia-smi --query-gpu=compute_cap --format=csv,noheader
```

## Manual install from source

1. **Go:** Install Go 1.22 or higher.
2. **Clone and build:**

   ```bash
   git clone https://github.com/flockadoo/flockadoo.git
   cd flockadoo
   go build -o flockadoo ./cmd
   ```

3. Run **`flockadoo setup`** so it writes config and can install the engine. Do not copy `config.yaml.example` by hand unless you are skipping the wizard on purpose.
4. **Run:**

   ```bash
   ./flockadoo --config ~/.config/flockadoo/config.yaml
   ```

The client opens an outbound connection to Flockadoo. No need to install ngrok or open firewall ports.

## Team Flocks

Linux is the only platform for a Team Flock. Setup downloads **winglink**, may ask for your password (`winglink needs root to create winglink0`), and prints **Winglink address** when this machine is on the private network. It does not start vLLM. See [Team Flocks](../provider/team-flocks.md).

## Related

- [Setup wizard](setup.md)
- [Team Flocks](../provider/team-flocks.md)
- [Installation](../getting-started/installation.md)
- [Configuration](configuration.md)
- [Setup: macOS](setup-mac.md)
- [Setup: Windows](setup-windows.md)
