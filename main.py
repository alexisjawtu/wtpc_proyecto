import numpy as np

from environment import Environment
from lion import Lion
from gazelle import Gazelle

def random_direction():
    dire = np.array([[1,0],[0,1],[-1,0],[0,-1]])
    return dire[np.random.randint(4)]

#Enviroment
width   = 200
height  = 200
env     = Environment(width,height)
#Lions and gazelles
num_lion    = 10
num_gazelle = 150
#Lion parameters
step_lion     = 3
hunger_lion   = 0
rad_lion      = 4
prob_at       = 0.6
hunger_delta  = 3
sleep         = 10 
# Gazzelle parameters
step_gazelle  = 4
hunger_gaz    = 0
gazelle_mass  = 25
#Initialize Lions and Gazelle
 
gazelles = env.herd_gazelle(num_gazelle, gazelle_mass, step_gazelle, hunger_gaz)
lions =	env.herd_lion(num_lion, step_lion, hunger_lion, rad_lion, prob_at)


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
            if not lion.is_idle():
                lion.set_hunger(lion.get_hunger() + hunger_delta)

                list_target = lion.get_targets()
                for target in list_target:
                    if lion.is_hungry():
                        lion.attack(gazelles[target])

            else:
                lion.decr_sleep_timer()

            lion.move_rnd(np.random.randint(3), np.random.randint(4), x_m, y_m)
            lions_out[k] = np.concatenate((np.array([1,k]), lion.get_position()))

        for j,gaz in enumerate(gazelles):
            gaz.move_rnd(np.random.randint(3), np.random.randint(4), x_m, y_m)
            if gaz.get_alive():
                gaz_out.append([0,j]+gaz.get_position().tolist())
        
        t = t+1
        np.savetxt(out,lions_out,fmt="%d",delimiter='\t')
        np.savetxt(out,np.array(gaz_out),fmt="%d",delimiter='\t')
        out.write("\n\n")