import numpy as np
from plot import plot_frame

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
step_lion     = 3
hunger_lion   = 50
rad_lion      = 3
prob_at       = .8
hunger_delta  = 4
sleep         = 4 
# Gazzelle parameters
step_gazelle  = 4
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

lion_quant = np.zeros(T)
gaze_quant = np.zeros(T)

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
                    if gazelles[target].get_alive() and lion.is_hungry():
                        lion.attack(gazelles[target])
            else:
                lion.decr_sleep_timer()
            lion.move_2(1,np.random.randint(4), x_m, y_m)

        for j,gaz in enumerate(gazelles):
            if gaz.get_alive():
                gaz_out.append([0,j]+gaz.get_position().tolist())
            gaz.move_2(1,np.random.randint(4), x_m, y_m)
        #if t%10 == 0:
        np.savetxt(out,lions_out,fmt="%d",delimiter='\t')
        lion_quant[t] = lions_out.shape[0]
        np.savetxt(out,np.array(gaz_out),fmt="%d",delimiter='\t')
        gaze_quant[t] = len(gaz_out)
        out.write("\n")
        t = t+1
file_txt = open("log.txt")
plot_frame(0, 0, x_m, y_m, file_txt, lion_quant, gaze_quant)
