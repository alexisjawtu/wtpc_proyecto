import matplotlib.pyplot as pp

def plot_frame(x0, y0, x1, y1, file_txt):
	#Opens file containing data to plot.
	datos_plot = file_txt
	lion_col = 'red'
	gazelle_col = 'blue'
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
			pp.xlim(x0-1, x1+1)
			pp.ylim(y0-1, y1+1)
			pp.title("Lions: " + lion_col + '. ' + "Gazelles: " + gazelle_col)

			for i in range(N):
				if spc_id[i] == 0: #If species is gazelle.
					pp.scatter(x_pos[i], y_pos[i], color = gazelle_col) #Blue for gazelles.
				else:
					pp.scatter(x_pos[i], y_pos[i], color = lion_col) #Red for lions.

			#Defines the file name for the frame and saves it.
			fig_name = "plot%d.png" % fig
			pp.savefig(fig_name, format='png')
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

