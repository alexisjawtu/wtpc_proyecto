import numpy as np
from animal import *

class Gazelle (Animal):
    
    def __init__ (self, position, alive = True):
        """TODO do not fix step nor hunger"""
        Animal.__init__(self, position, 3, 30, alive)

