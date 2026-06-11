import numpy as np
import matplotlib.pyplot as plt
import os

# Set interactive mode
plt.ion()

import guessResonanceFrequenciesBen as grf
import fitresonance as fr

# Resolve robust relative paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.normpath(os.path.join(script_dir, "..", "data", "widesurvey_aSi80s_20240913.npz"))
plots_dir = os.path.normpath(os.path.join(script_dir, "..", "plots"))

print(f"Loading data from: {data_path}")
temp = np.load(data_path)
f = temp["f_wide"]
s21 = temp["s21_wide_35"]

# Remove cable delay linear phase trend
pf = np.polyfit(f, np.unwrap(np.angle(s21)), deg=1)
s21 = s21 * np.exp(1j*(-pf[0]*f + -pf[1]))

# Restrict size for faster analysis
f = f[:100000]
s21 = s21[:100000]

# Plot transmission
plt.figure(111, figsize=(7,5))
plt.plot(f/1e9, 20*np.log10(np.abs(s21)) + 1)
plt.xlim(5.3, 6.5)
plt.xlabel("Frequency (GHz)")
plt.ylim(-30, 0 + 10.0)
plt.ylabel("|S21| (dB)")

bw_lo = 100e3
bw_hi = 200e3
print("Running resonance frequency candidate search...")
# Run non-interactively
tau, good, f0good = grf.guess_resonance_frequencies(
    f, s21, bw_lo, bw_hi, 
    threshold_diam=0.05, 
    threshold_spacing=2.0, 
    threshold_circlefiterr=0.1, 
    interactive=False
)

nres = len(good)
print(f"Fitting resonance curves for {nres} identified resonators...")
f0fits = np.zeros(nres)
Qcfits = np.zeros(nres)
Qifits = np.zeros(nres)
for n in range(nres):
    ftemp = f[good[n]-100:good[n]+100]
    s21temp = s21[good[n]-100:good[n]+100]
    try:
        f0fittemp, Qcfittemp, Qifittemp = fr.fit_resonance(ftemp, s21temp, showplot=False)
        f0fits[n] = f0fittemp
        Qcfits[n] = Qcfittemp
        Qifits[n] = Qifittemp
    except Exception as e:
        print(f"Fitting failed on resonator {n}: {e}")
        f0fits[n] = 0.0
        Qcfits[n] = 0.0
        Qifits[n] = 0.0

# Plot Q-factor results
plt.figure(222, figsize=(7,7))
plt.subplot(2,1,1)
plt.semilogy(f0fits/1e9, Qifits/1e3, "o")
plt.xlim(5.2, 6.5)
plt.xlabel("Frequency (GHz)")
plt.ylim(10, 2e3)
plt.ylabel("Qi/1000")
plt.subplot(2,1,2)
plt.hist(Qifits/1e3, bins=np.arange(0, 2000, 100))
plt.xlim(0, 2e3)
plt.xlabel("Qi/1000")

# Save figures
fig1_path = os.path.join(plots_dir, "s21_transmission.png")
fig2_path = os.path.join(plots_dir, "quality_factors.png")

plt.figure(111)
plt.savefig(fig1_path, dpi=150, bbox_inches='tight')
plt.figure(222)
plt.savefig(fig2_path, dpi=150, bbox_inches='tight')

print("=========================================")
print("Analysis complete!")
print(f"Saved plots to:\n  - {fig1_path}\n  - {fig2_path}")
print("=========================================")
