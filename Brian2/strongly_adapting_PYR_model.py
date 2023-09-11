'''
Strongly adapting PYR model
@author: Ferguson et al. (2014) F1000Res. 
'''
from brian2 import *

defaultclock.dt = 0.002*ms

#Strongly adapting PYR parameters
C=115 * pF
vr=-61.8 * mV
vpeak=22.6 * mV
c=-65.8 * mV
klow=0.1 * nS/mV
khigh=3.3  * nS/mV
a=0.0012 /ms
d=10 * pA
vt=-57.0 *mV
b=3 * nS

N=1   #number of cells
mean_Iapp=100 #mean Iapplied input
Ishift_raw=0  # Ishift

time=0

#cell eqns
pyr_eqs = """
Iext  : amp
Ishift : amp
k=int(v<vt)*klow + int(v>=vt)*khigh : siemens/volt
du/dt = a*(b*(v-vr)-u)            : amp
dv/dt = (k*(v-vr)*(v-vt)+Ishift+Iext -u)/C : volt
"""

#define neuron group
PYR = NeuronGroup(N, model=pyr_eqs, reset ="v = c; u += d" , threshold="v>=vpeak")

#set excitatory drive 
PYR.Iext = mean_Iapp*pA

#set Ishift
PYR.Ishift = Ishift_raw*pA

#set initial conditions for each neuron
###PYR.v = rand(len(PYR))*0.01 -0.065 # Removing random init in single cell case
PYR.v = -65*mV

#record all spike times for the neuron group
PYR_v = StateMonitor(PYR, 'v', record=True)

#run for x seconds of simulated time
duration = 1 * second  # 0.01 * second

#create arrays to record network output
times = zeros(int(duration/defaultclock.dt) +1)
voltage = zeros(int(duration/defaultclock.dt) +1)

net =Network(PYR,PYR_v) 
net.run(duration)


####make voltage plot####
import sys
if not '-nogui' in sys.argv:
    plot(PYR_v.t,PYR_v[0].v/mV)
    xlabel("Time (s)")
    ylabel("Membrane Potential (mV)")
    title('Strongly adapting PYR model with %d pA input'%(mean_Iapp))
    show()
    
####save trace to file####
save=True
if save:
    filename = 'Strong.v.dat'
    outfile = open(filename,'w')
    t = PYR_v.t/second
    v = PYR_v[0].v/volt
    print("Saving results to: %s"%filename)
    for i in range(len(t)):
        line = '%s\t%s\n'%(t[i], v[i])
        outfile.write(line)
    outfile.close()
