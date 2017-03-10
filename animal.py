import numpy as np

dire = np.array([[1,0],[0,1],[-1,0],[0,-1]])

class Animal (object):
    """Animal(pos) -> new living animal standing at position pos."""
    def __init__ (self, position, step = 1, hunger = 50, alive = True):
        """ np.array[2] position, 
            integer step
            integer hunger, between 1 and 100 and
            boolean set_alive"""
        self.position   = position
        self.step       = step
        self.hunger     = hunger
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
        res_pos = self.position + self.step*n*dire[direc]
        
        es tan solo (x + delta )%size



        if res_pos[0] < 0 or res_pos[0] > env_h or \
            res_pos[1] < 0 or res_pos[1] > env_h:

            if direc % 2 == 0:  env_size = env_w
            else:               env_size = env_h
            
            (q, r)  = divmod(res_pos[direc%2], env_size)
            delta   = wall - x - r
            if q % 2 == 1:
                res_pos[direc%2] = r desde el opuesto
            else:
                res_pos[direc%2] = r desde e
        
        self.position = res_pos
        
    def move_rnd (self, n_random, direction, env_w, env_h):
        """ direction == [1,0], [0,1], [-1,0], [0,-1] 
            TODO: si sobra rebota con tamano de environment
        """
        self.position += self.step*n_random*direction

    def eat (self, food):
        self.hunger = min (self.hunger - food, 0)        
