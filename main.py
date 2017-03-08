import numpy as np

params_list_l   = []
params_list_g   = []
lions           = []
gazelles        = []
for p in params_list_l:
    lions.append(Lion(p))
for p in params_list_g:
    gazelles.append(Gacel(p))

medium = Envorinment(__args__)

t = 0
T = 100
while t < T:
    medium.

