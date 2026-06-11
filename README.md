# Resonator Survey

A Python project for taking and analyzing wide frequency-swept surveys of superconducting resonators using a Vector Network Analyzer (VNA).

## Repository Overview

This repository contains scripts and modules for measuring and fitting superconducting resonator data:

*   **`widesurvey.py`**: Controls a VNA to measure wide frequency surveys at different power levels and saves the data.
*   **`frsurvey.py`**: Performs flux-ramp sweeps of identified resonators using a VNA and battery bias source.
*   **`quickanalysis1.py`**: Fits the resonance data to a circle in the complex plane to extract the resonance frequency $f_0$, coupling quality factor $Q_c$, and internal quality factor $Q_i$.
*   **`guessResonanceFrequenciesBen.py`**: Identifies candidate resonance frequencies from transmission data ($S_{21}$).
*   **`fitresonance.py`**: Implements circle-fitting algorithms (Taubin algebraic fit) and Lorentz/arctan models to fit transmission data.
*   **`ben_find_peaks.py`**: Utility to identify local maxima in resonance data with minimum peak separation.

---

## Setup & Installation

This project is configured using [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver.

### Prerequisites

Ensure you have `uv` installed. If not, install it via:

```bash
# On Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex

# On macOS/Linux
curl -FsSL https://astral.sh/uv/install.sh | sh
```

### Initializing Environment

To initialize the environment and sync all required dependencies (like `numpy`, `scipy`, and `matplotlib`), run:

```bash
uv sync
```

This will automatically create a `.venv` virtual environment and install the correct package versions.

### Running Scripts

To run any of the analysis or survey scripts within the configured environment:

```bash
uv run quickanalysis1.py
```
