import numpy as np
from animal import *

class Lion (Animal):
    
    def __init__ (self, position, step = 1, hunger = 50, hunger_tol = 20, radius = 1, attack_prob=0.8, \
        targets = np.array([], dtype = int), alive = True):
        """ attack_prob must be a uniform random number in (.5,1)
            targets is an 1D np.array. To operate, consider proper transposings
            after concatenation.

            radius == the radius of the attack region of the Lion

         """
        Animal.__init__ (self, position, step, hunger, hunger_tol, alive)
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
        self.targets = np.concatenate((self.targets, [index]))

    def is_hungry (self):
        """ Returns whether the lion is hungry. Makes a comparison between
        Lion.hunger and Lion.hunger_tol. """
        if self.hunger > self.hunger_tol:   hunger = True
        else:                               hunger = False
        return hunger

    def attack (self, g):
        """ takes the gazelle and kills and occupies its position
            according to the attack_prob """
        p = np.random.random()
        if (self.attack_prob > p):
            self.set_position(g.position)
            # TODO: something with the mass of the gazelle?
            # g.mass == 25
            self.eat(25) 
            g.alive = False
        return
    
