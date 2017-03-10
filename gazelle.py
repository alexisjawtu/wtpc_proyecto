import numpy as np
from animal import *

class Gazelle (Animal):
    
    def __init__ (self, position, step = 1, hunger = 50, alive = True):
        """ Gazelle is, basically, an animal"""
        Animal.__init__(self, position, step, hunger, alive)

