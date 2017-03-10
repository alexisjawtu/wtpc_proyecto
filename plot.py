import matplotlib.pyplot as pp

def plot_frame(x0, y0, x1, y1):
	#Opens file containing data to plot.
	datos_plot = open('log.txt')

	#Creates lists to read file elements
	spc_id = [] #Species ID;
	idv_id = [] #Individual ID; 
	x_pos = []  #X position;
	y_pos = []  #Y position;

	#Animals amount.
	N = 0
	#Frame number.
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
			#Creates a frame and axis.
			pp.figure()
			pp.axis([x0, y0, x1, y1])

			for i in range(N):
				if spc_id[i] == 0: #If species is gazelle.
					pp.plot(x_pos[i], y_pos[i], 'b^') #Blue for gazelles.
				else:
					pp.plot(x_pos[i], y_pos[i], 'r*') #Red for lions.

			#Defines the file name for the frame and saves it.
			fig_name = "plot%d.jpg" % fig
			pp.savefig(fig_name)
			fig+=1
			pp.close()

			#Clears all list to load the next frame.
			spc_id[:] = []
			idv_id[:] = []
			x_pos[:] = []
			y_pos[:] = []
			N = 0
		
	#Closes file.
	datos_plot.close()

