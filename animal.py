import numpy as np

class Animal (object):
    """ documentation here please """
    def __init__ (self, position, step = 1, hunger = 50, alive = True):
        """ position is np.array[2] 
            step is integer
            hunger is integer between 1 and 100
            alive is True or False
        """
        self.position   = position
        self.step       = step
        self.hunger     = hunger
        self.alive      = alive

    def set_position (self, pos):
        self.position = pos

    def get_position (self):
        return self.position

    def move (self, n_random, direction):
        """ direction == [1,0], [0,1], [-1,0], [0,-1] """
        self.position += self.step*n_random*direction

    def eat (self):
        pass        