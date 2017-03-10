import numpy as np

dire = np.array([[1,0],[0,1],[-1,0],[0,-1]])
""" dire: cardinal points """

class Animal (object):
    """Animal(pos) -> new living animal standing at position pos."""
    def __init__ (self, position, step, hunger, hunger_tol, is_full, alive = True):
        """ np.array[2] position,
            integer step
            integer hunger, between 1 and 100 and
            integer hunger, between 1 and 100 and
            boolean is_full: true if and only if the animal eat during the previous iteration.
            boolean set_alive"""
        self.position   = position
        self.step       = step
        self.hunger     = hunger
        self.hunger_tol = hunger_tol
        self.alive      = alive

    def set_position (self, pos):
        self.position = pos

    def get_position (self):
        return self.position

    def set_step (self, step):
        self.step = step

    def get_step (self):
        return self.step

    def set_hunger (self, hunger):
        self.hunger = hunger

    def get_hunger (self):
        return self.hunger

    def set_is_full (self, is_full):
        self.is_full = is_full

    def get_is_full (self):
        return self.is_full

    def set_alive (self, alive):
        self.alive = alive

    def get_alive (self):
        return self.alive

    def move (self, n, direc, env_w, env_h):
        """ 
        Moves the animal n steps with direction direc, keepeing the
        animal within the environment.
        
        Parameters
        ----------
        n: integer.
        number of steps.
        direc: np.array 
        with values [1,0], [0,1], [-1,0] or [0,-1], like NSEW.
        env_w and env_h: integers.
        width and height of the environment.
        """
        res_pos         = self.position + self.step*n*dire[direc]
        res_pos[0]      = env_h - (res_pos[0] % env_h)
        res_pos[1]      = env_w - (res_pos[1] % env_w)
        self.position   = res_pos
  
#    def move_2 (self, n, direc, env_w, env_h):
#        """ direction == [1,0], [0,1], [-1,0], [0,-1] """
#        res_pos = self.position + self.step*n*direc
#
#        if (res_pos[0] < 0) or (res_pos[0] > env_w):
#    		if res_pos[0]<0:
#    			res_pos[0] = -res_pos[0]
#		else:
#			res_pos[0] = 2*env_w - res_pos[0]
#        if (res_pos[1] < 0) or (res_pos[1] > env_h):
#            if res_pos[1]<0:
#                res_pos[1] = -res_pos[1]
#		else:
#			res_pos[1] = 2*env_h - res_pos[1] 
#        self.position = res_pos
        
    def move_rnd (self, n_random, direction, env_w, env_h):
        """ direction == [1,0], [0,1], [-1,0], [0,-1] 
            TODO: si sobra rebota con tamano de environment
        """
        self.position += self.step*n_random*direction

    def eat (self, food):
        self.hunger     = min (self.hunger - food, 0)
        self.is_full    = True        
