import os
import sys

def main():
    print("=========================================")
    print("         Resonator Survey Tool           ")
    print("=========================================")
    print("\nThis repository contains the following modules (in src/):")
    print("  - widesurvey.py      : Measure wide frequency sweeps using VNA.")
    print("  - frsurvey.py        : Perform flux-ramp surveys.")
    print("  - quickanalysis1.py  : Fit transmission data to complex circles.")
    print("  - fitresonance.py    : Fitting algorithms and utilities.")
    print("\nTo run the quick analysis example:")
    print("  uv run src/quickanalysis1.py")
    print("\nFor setup instructions, please read README.md.")
    print("=========================================")

if __name__ == "__main__":
    main()
