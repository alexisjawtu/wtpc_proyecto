import numpy as np
from animal import *

class Lion (Animal):
    
    def __init__ (self, position, radius, attack_prob, \
        targets = np.array([], dtype = int), alive = True):
        Animal.__init__ (self, position, 2, 80, alive)
        """ attack_prob must be a uniform random number in (.5,1) """
        self.radius      = radius
        self.attack_prob = attack_prob
        self.targets     = targets

    def set_radius (self, rad):
        self.radius = rad

    def get_radius (self):
        return self.radius

    def set_attack_prob (self, rad):
        self.attack_prob = rad

    def get_attack_prob (self):
        return self.attack_prob

    def set_targets (self, tar):
        self.targets = tar

    def get_targets (self):
        return self.targets

    def add_target (self, index):
        self.set_targets(np.concatenate((self.get_targets(), [index])))

    def attack (self, g):
        """ takes the gazelle and kills and occupies its position
            according to the attack_prob """
        p = np.random.random()
        if (attack_prob > p):
            self.set_position (g.position)
            # TODO: something with the mass of the gazelle?
            # g.mass == 25
            self.hunger     = min(self.hunger - 25, 0) 
            g.alive         = False
        return