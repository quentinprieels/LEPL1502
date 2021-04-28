import numpy as np
from matplotlib import pyplot as plt 

def vl(t):
    vl = np.sin(t)
    return vl 

def vamp(vl,pramp,ramp):
    for i in range(len(vl)):
        if vl[i]<= 0 :
            vl[i]=0
    v = vl*(1+(pramp/ramp))
    return v    

ramp = 5600
t = np.linspace(-10,10,1000)
Vl = 0.4 * vl(t)
pramp = 50400

y = vamp(Vl,pramp,ramp) 
Vamp = plt.plot(t,y,'r', label ='V_amp')
sin = plt.plot(t,0.4*vl(t),'b', label = 'V_L')
plt.ylim(-1,5)
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.legend(loc = 'upper right')
plt.show()
