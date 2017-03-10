import numpy as np

from environment import Environment
from lion import Lion
from gazelle import Gazelle

def random_direction():
    dire = np.array([[1,0],[0,1],[-1,0],[0,-1]])
    return dire[np.random.randint(4)]

#Enviroment
width   = 600
height  = int(width/1.618)
env     = Environment(width,height)
#Lions and gazelles
num_lion    = 15
num_gazelle = 200
#Lion parameters
step_lion     = 4
hunger_lion   = 50
rad_lion      = 100
prob_at       = 1
hunger_delta  = 3
sleep         = 3 
# Gazzelle parameters
step_gazelle  = 6
hunger_gaz    = 0
gazelle_mass  = 8
#Initialize Lions and Gazelle
 
gazelles = env.herd_gazelle(num_gazelle, gazelle_mass, step_gazelle, hunger_gaz)
lions =	env.herd_lion(num_lion, step_lion, hunger_lion, rad_lion, prob_at)


#Time Loop
f_name = 'log.txt'

t = 0
T = 1000

x_m = env.get_width()
y_m = env.get_height()

with open (f_name, "w") as out:
    while t < T:
        env.map_positions(lions, gazelles)
        lions_out = np.zeros((num_lion,4))
        gaz_out = []
        for k, lion in enumerate(lions):
            lions_out[k] = np.concatenate((np.array([1,k]), lion.get_position()))
            if not lion.is_idle():
                lion.set_hunger(lion.get_hunger() + hunger_delta)

                list_target = lion.get_targets()
                for target in list_target:
                    if lion.is_hungry():
                        lion.attack(gazelles[target])

            else:
                lion.decr_sleep_timer()

            lion.move_2(1,np.random.randint(4), x_m, y_m)

        for j,gaz in enumerate(gazelles):
            if gaz.get_alive():
                gaz_out.append([0,j]+gaz.get_position().tolist())
            gaz.move_2(1,np.random.randint(4), x_m, y_m)
        if t%10 == 0:
            np.savetxt(out,lions_out,fmt="%d",delimiter='\t')
            np.savetxt(out,np.array(gaz_out),fmt="%d",delimiter='\t')
            out.write("\n")
        t = t+1