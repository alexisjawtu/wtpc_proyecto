import numpy as np

from  environment import Environment
from lion import Lion
from gazelle import Gazelle

def random_direction():
    dire = np.array([[1,0],[0,1],[-1,0],[0,-1]])
    return dire[np.random.randint(4)]

#Enviroment

width = 200
height= 200
env = Environment(width,height)

#Lions and gazelles

num_lion = 50
num_gazelle = 150

#Lion parameters
 
stepLion = 3
hungerLion = 0
radLion = 4
probAt = 0.6

# Gazzelle parameters

stepGazelle = 4
hungerGaz = 0

#Initialize Lions and Gazelle
 
gazelles = env.herd_gazelle(num_gazelle, stepGazelle, hungerGaz)
lions =	env.herd_lion(num_lion, stepLion, hungerLion, radLion, probAt)


#Time Loop
f_name = 'log.txt'

t = 0
T = 500

with open (f_name, "w") as out:
    while t < T:
        env.map_positions(lions, gazelles)
        
        lions_out = np.zeros((num_lion,4))
        gaz_out = []
	x_m = env.get_width()
	y_m = env.get_height()
        
        for k, lion in enumerate(lions):
            list_target = lion.get_targets()
            for target in list_target:
                lion.attack(gazelles[target])
            lion.move_2(1, random_direction(), x_m, y_m)
            lions_out[k] = np.concatenate((np.array([1,k]),lion.get_position())) 

        for j,gaz in enumerate(gazelles):
            gaz.move_2(1, random_direction(), x_m, y_m)
            if gaz.get_alive():
                gaz_out.append([0,j]+gaz.get_position().tolist())
        
        t = t+1
        np.savetxt(out,lions_out,fmt="%d",delimiter='\t')
        np.savetxt(out,np.array(gaz_out),fmt="%d",delimiter='\t')
        out.write("\n\n")
        
