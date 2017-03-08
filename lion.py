import numpy as np

class Lion (Animal):

    def __init__ (self, radius, attack_prob, targets = np.array([], dtype = int)):
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

    def attack (self, g_index):
        """ takes the gazelle index and kills and occupies its position
            according to the attack_prob """
        if (probability test):
            pass
 