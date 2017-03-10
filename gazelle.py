import numpy as np
from animal import *

class Gazelle (Animal):
    """Gazelle(pos) -> new living gazelle standing at position pos."""
    def __init__ (self, position, gazelle_mass = 25, step = 1, hunger = 50, alive = True):
		""" np.array[2] position,
            integer gazelle_mass,
            integer step,
            integer hunger, between 1 and 100
            boolean alive. """
        Animal.__init__(self, position, step, hunger, alive)
        self.gazelle_mass = gazelle_mass
