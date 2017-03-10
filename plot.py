import matplotlib.pyplot as pp

#Opens file containing data to plot.
datos_plot = open('log.txt')

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
		pp.axis([0, 600, 0, 123])
		for i in range(N):
			if spc_id[i] == 0: #Si la especie es gacela.
				pp.scatter(x_pos[i], y_pos[i]) #Gacelas en azul.
			else:
				pp.scatter(x_pos[i], y_pos[i], color='red') #Leones en rojo.
		fig_name = "plot%d.png" % fig
		fig+=1
		pp.savefig(fig_name, format='png')
		
		spc_id[:] = [] #
		idv_id[:] = [] #
		x_pos[:] = []  #
		y_pos[:] = []  #
		N = 0
	pp.close()
#Closes file.
datos_plot.close()

