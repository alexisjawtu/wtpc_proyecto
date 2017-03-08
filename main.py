import numpy as np

params_list_l   = []
params_list_g   = []
lions           = []
gazelles        = []
for p in params_list_l:
    lions.append(Lion(p))
for p in params_list_g:
    gazelles.append(Gacel(p))

env = Envorinment(__args__)

t = 0
T = 100
while t < T:
    env.map_positions (lions, gazelles)
    for lion in lions:
        lion.attack()
        lion.move()
    for gaz in gazelles:
        

