import numpy as np

from  environment import Environment
from lion import Lion
from gazelle import Gazelle
#Enviroment

width = 20
height= 20
env = Environment(width,height)

#Lions and gazelles

num_lion = 10
num_gazelle = 30

# Lion parameters
 
stepLion = 3
hungerLion = 0
radLion = 4
probAt = np.random.random()*.5 +.5

# Gazzelle parameters

stepGazelle = 1
hungerGaz = 0

#Initialize Lions and Gazelle
 
lions = []
gazelles = []
for p in range(num_lion):
	PosL = np.array([np.random.randint(width),np.random.randint(height)])
	lions.append(Lion(PosL, radLion, probAt))

for p in range(num_gazelle):
	PosGaz = np.array([np.random.randint(width),np.random.randint(height)])
	gazelles.append(Gazelle(PosGaz))

def random_direction():
    dire = np.array([[1,0],[0,1],[-1,0],[0,-1]])
    return dire[np.random.randint(4)]

#Time Loop
f_name = 'log.txt'

t = 0
T = 10

with open (f_name, "w") as out:
    while t < T:
        env.map_positions(lions, gazelles)
        
        lions_out = np.zeros((num_lion,4))
        gaz_out = []
        
        for k, lion in enumerate(lions):
            list_target = lion.get_targets()
            for target in list_target:
                lion.attack(gazelles[target])
            lion.move_rnd(1, random_direction(), env.get_width(), env.get_height())
            lions_out[k] = np.concatenate((np.array([1,k]),lion.get_position())) 
        for j,gaz in enumerate(gazelles):
            gaz.move_rnd(1, random_direction(), env.get_width(), env.get_height())
            if gaz.get_alive():
                gaz_out.append([0,j]+gaz.get_position().tolist())
        
        t = t+1
        np.savetxt(out,lions_out,fmt="%d",delimiter='\t')
        np.savetxt(out,np.array(gaz_out),fmt="%d",delimiter='\t')
        out.write("\n")
        