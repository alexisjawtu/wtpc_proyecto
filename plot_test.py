import numpy as np
import scipy
import matplotlib.pyplot as pp
from pylab import *

f_out_max = open('tabla.txt', 'w')

x=arange(441)
sin1 = 1*sin(2*pi*(25/441.0)*x)
sin2 = 0.25*sin(2*pi*((25./2)/441.0)*x)
sig = sin1+sin2

print 'x: ',x
print 'sig:', sig
vec = np.c_[x,sig]

print 'vec: ',vec
np.savetxt(f_out_max,vec,fmt='%f',delimiter='\t',header="x #f(x)")
f_out_max.close()

pp.figure()
pp.plot(x*1./44100.,sig, color='r',label='Time signal VS')
pp.ylabel('Amplitude')
pp.grid(True)
pp.xlabel('Time (s)')
pp.show()

