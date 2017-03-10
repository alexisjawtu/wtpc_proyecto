import time
import numpy as np
import scipy
import matplotlib.pyplot as pp
from pylab import *

#Opens file containing data to plot.
datos_plot = open('prueba_plot.txt')

#Creates lists to read file elements
spc_id = [] #Species ID;
idv_id = [] #Individual ID; 
x_pos = []  #X position;
y_pos = []  #Y position;

#Animals amount.
N = 0

#Plots a frame.
#pp.ion()

fig = 0
#Loads data from file to lists.
for line in datos_plot:
	if line != "\n":
		spc_id.append(int(line.split("\t")[0]))
		idv_id.append(line.split("\t")[1])
		x_pos.append(line.split("\t")[2])
		y_pos.append(line.split("\t")[3])
		N+=1
	else:
		pp.figure()
		pp.axis([0, 50, 0, 50])
		for i in range(N):
			if spc_id[i] == 0: #Si la especie es gacela.
				pp.plot(x_pos[i], y_pos[i], 'b^') #Gacelas en azul.
			else:
				pp.plot(x_pos[i], y_pos[i], 'r*') #Leones en rojo.
		fig_name = "plot%d.jpg" % fig
		fig+=1
		pp.savefig(fig_name)
		
		spc_id[:] = [] #
		idv_id[:] = [] #
		x_pos[:] = []  #
		y_pos[:] = []  #
		N = 0
		
#Closes file.
datos_plot.close()

