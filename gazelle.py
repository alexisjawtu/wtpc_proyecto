import numpy as np
from animal import *

class Gazelle (Animal):
    
    def __init__ (self, position, alive = True):
        Animal.__init__(self, position, 3, 30, alive)

