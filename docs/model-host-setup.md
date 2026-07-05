# Model Host Setup

## Hardware
- HP Z840 workstation — dual Xeon E5-2680v3 (24c/48t), 128 GB RAM
- GPU: NVIDIA Quadro M4000 (8 GB GDDR5, Maxwell, compute capability 5.2)
- Storage: 4x 1 TB SSD (OS on sda; sdb/sdc/sdd pooled for data)

## Operating system
- Ubuntu 24.04 LTS

## GPU driver
- Proprietary `nvidia-driver-580` (last branch supporting Maxwell).
- Installed the `-server` variant; held at 580 to avoid an upgrade to 590+
  (which dropped Maxwell support).
- Verified with `nvidia-smi` (driver 580.x, 8192 MiB visible) and confirmed
  models run on GPU via `ollama ps` (PROCESSOR column = 100% GPU for 8B models).

## Inference stack
- Ollama (built on llama.cpp), OpenAI-compatible API on port 11434.
- Runs as a systemd service (auto-starts; no manual `ollama serve` needed).
- Two-tier model strategy: small (7B-8B) models on the GPU for interactive use,
  large (70B) models on CPU across system RAM for overnight batches.

## Notes / lessons learned
- The `-open` NVIDIA driver does NOT support Maxwell; the proprietary branch is required.
- vLLM and Flash Attention are not usable on this card (need newer compute capability).
