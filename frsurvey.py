import numpy as np
import time
import sys
import guessResonanceFrequencies as grf
import alyE5071B_usb
import srs_sim900
import srs_sim928
import matplotlib.pyplot as plt
plt.ion()

############################################################################################################

# User-defined parameters:
f_lo = 3.7e9                        # Start frequency of wide survey (Hz).
f_hi = 5.4e9                        # End frequency of wide survey (Hz).
expbw = 10e6                        # Expected resonance bandwidth (Hz).
fspan = 4*expbw                     # Frequency span of flux-ramp surveys (Hz).
vbias = np.arange(0.0,2.5,0.02)     # Battery voltage sweep values (V). I recommend a value that results in between 1 and 2 Phi0.
rbias = 2.02e3                      # Flux-ramp series resistance (Ohms).
filename = "frsurvey_wsquid_v2.1_w2_20220725.npz"   # Name of file to save the data.

############################################################################################################

# Initialize VNA and battery box
vna = alyE5071B_usb.alyE5071B_usb()
mainframe = srs_sim900.SRS_SIM900(port='/dev/ttyUSB0',baudrate=9600)
bb = srs_sim928.SRS_SIM928(mainframe,sim_port=1)

# Take wide VNA survey
tempdata = vna.measureSurvey(fi=f_lo/1e6,ff=f_hi/1e6,fres=0.01,power=-55,mtype='S21',averfact=4)
f_wide = tempdata[:,0]*1e6
s21_wide = tempdata[:,1] + 1j*tempdata[:,2]
np.savez(filename,f_wide=f_wide,s21_wide=s21_wide)

# Identify resonances
tau,good,fc = grf.guessResonanceFrequencies(f_wide,s21_wide,bw=expbw,threshold=0.7)
print("{:d} resonators found.".format(len(good)))
good = np.sort(good)
fc = np.sort(fc)
#fc = fc[0:2]

# Perform flux-ramp survey of each identified resonance
npts = 201
fbias = np.linspace(-fspan/2,fspan/2,npts)
ibias = vbias/rbias
s21_fr = np.zeros((fc.size,vbias.size,npts),dtype='complex')

bb.setvolt(0.0)
time.sleep(1.0)

#plt.figure()                # Updating (per resonator) color plot of S21 surface for sanity check
for k in range(fc.size):
    bb.setvolt(0.0)
    time.sleep(1.0)
    for l in range(vbias.size):
        bb.setvolt(vbias[l])            # Set bias voltage
        ftemp = fc[k] + fbias
        sys.stdout.write('\rResonator %d : Voltage %03.2f'%((k+1),vbias[l]))
        sys.stdout.flush()
        time.sleep(0.5)
        tempdata = vna.alySnapShot(fi=ftemp[0]/1e6, ff=ftemp[-1]/1e6, power=-55, mtype='S21', numpts=npts, averfact=4)  # Take VNA snapshot
        s21_fr[k,l,:] = (tempdata[:,1]+1j*tempdata[:,2]) * np.exp(2j*np.pi*tau*ftemp)                                   # Remove cable-delay
    # Save the data
    np.savez(filename,f_wide=f_wide,s21_wide=s21_wide,fc=fc,ibias=ibias,fbias=fbias,s21_fr=s21_fr,tau=tau)
#    plt.clf()
#    plt.imshow(np.transpose((np.abs(s21_fr[k,:,:]))/np.max(np.abs(s21_fr[k,:,:]))),cmap='Greys',interpolation="Nearest",aspect='auto')
#    plt.draw()

bb.setvolt(0.0)
