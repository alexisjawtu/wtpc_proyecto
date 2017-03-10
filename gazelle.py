import numpy as np
from animal import *

class Gazelle (Animal):
    
    def __init__ (self, position, step = 1, hunger = 50, rep_prob = 0.1, repro = np.array([], dtype = int), alive = True):
        """ Gazelle is, basically, an animal"""

	stepG = step + np.random.randint(-1,1) 
	hungerG = np.random.normal(hunger,3)

        Animal.__init__(self, position, stepG, hungerG, alive)
	self.repro = repro
	self.rep_prob = rep_prob
	
    def add_repro (self, index):
	self.repro = np.concatenate((self.repro, [index]))
    
    def set_repro (self, rep):
        self.repro = rep

    def get_repro (self):
        return self.repro

    def reproduction(self, pups, position, stepGazelle, hungerGaz):
	p = np.random.random()
	if (self.rep_prob > p):
		pups.append(Gazelle(position,stepGazelle, hungerGaz))
	

	

