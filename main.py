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
num_gazzelle = 30

# Lion parameters
 
stepLion = 3
hungerLion = 0
radLion = 4
probAt = np.random.random()*.5 +.5

# Gazzelle parameters

stepGazzelle = 1
hungerGaz = 0

#Initialize Lions and Gazelle
 
lions = []
gazelles = []
for p in range(num_lion):
	PosL = np.array([np.random.randint(width),np.random.randint(height)])
	lions.append(Lion(PosL, radLion, probAt))

for p in range(num_gazzelle):
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
        for lion in lions:
            list_target = lion.get_targets()
            for target in list_target:
                lion.attack(gazelles[target])
            lion.move_rnd(1, random_direction(), env.get_width(), env.get_height())
        for gaz in gazelles:
            gaz.move_rnd(1, random_direction(), env.get_width(), env.get_height())
        
        t = t+1
        np.savetxt(out,np.array([1,2,3]))
        out.write("\n\n")
        
        