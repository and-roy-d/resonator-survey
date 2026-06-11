# Resonator Survey

A Python project for taking and analyzing wide frequency-swept surveys of superconducting resonators using a Vector Network Analyzer (VNA).

## Directory Structure

The repository has been structured as follows:

*   **`src/`**: Contains all Python source files (just code):
    *   `widesurvey.py`: Controls a VNA to measure wide frequency surveys at different power levels.
    *   `frsurvey.py`: Performs flux-ramp sweeps of identified resonators using a VNA and battery bias source.
    *   `quickanalysis1.py`: Runs non-interactive resonance analysis, fits data to complex circles, and saves plots.
    *   `guessResonanceFrequenciesBen.py`: Candidate resonance frequencies search module.
    *   `fitresonance.py`: Fits transmission data to circle and Lorentz/arctan models.
    *   `ben_find_peaks.py`: Peak-finding utilities.
    *   `main.py`: Repository CLI overview script.
*   **`data/`**: Directory for raw measurement data:
    *   `widesurvey_aSi80s_20240913.npz`: Example data file (saved to Git).
*   **`plots/`**: Directory for analysis plots:
    *   `s21_transmission.png`: Generated plot of $S_{21}$ transmission vs frequency.
    *   `quality_factors.png`: Generated plot of fit quality factors ($Q_i$).

---

## Setup & Installation

This project is configured using [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver.

### Prerequisites

Ensure you have `uv` installed. If not, install it via:

```bash
# On Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### Running Analysis (and Generating Plots)

Since your project folder is located inside a cloud-synced folder (like OneDrive or Dropbox), `uv`'s default hardlinking strategy fails. You must specify `--link-mode=copy` to use standard file copying.

To run the analysis:

Double-click or run the helper batch script (which automatically includes the copy flag):
```cmd
.\run_analysis.bat
```

Or run it manually in your terminal:
```bash
# Install dependencies
uv sync --link-mode=copy

# Run the script
uv run --link-mode=copy src/quickanalysis1.py
```

---

## Git & GitHub Setup

To clean up old files, commit the repository, and push it to GitHub, simply run the helper script:

```cmd
.\setup_git.bat
```

This script will:
1. Delete duplicate old files from the root directory.
2. Stage and commit all files (including the `data/` folder and analysis outputs).
3. Set the default branch to `main`.
4. Prompt you to push directly to your GitHub repository.
