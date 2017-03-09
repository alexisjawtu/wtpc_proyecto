import numpy as np
import random
from animal import Animal
from lion import Lion

#Enviroment

width = 20
height= 20
#env = Environment(width,height)

#Lions and gazelles

num_lion = 10
num_gazzelle = 30

# Lion parameters
 
stepLion = 3
hungerLion = 0
radLion = 4
probAt = 1

# Gazzelle parameters

stepGazzelle = 1
hungerGaz = 0

#Initialize Lions and Gazelle
 
lions = []
gazelles = []
for p in range(num_lion):
	PosL = np.array([random.randrange(width),random.randrange(height)])
	lion = Lion(PosL, stepLion, hungerLion, True, radLion, probAt)
	lions.append(lion)

for p in range(num_gazzelle):
	PosGaz = np.array([random.randrange(width),random.randrange(height)])
	gaz = Gazelle(PosGaz, stepGazzelle, hungerGaz, True)
	gazelles.append(gaz)


#Time Loop

t = 0
T = 100
while t < T:
	env.map_positions(lions, gazelles)
	for lion in lions:
		lion.attack()
		lion.move(env.get_width,env.get_height)
	for gaz in gazelles:
		gaz.move(env.get_width,env.get_height)
	t = t+1	

       

