class Animal (Object):
    
    def __init__ (self, position, step, hunger, alive):
        self.position = position
        self.step = step
        self.hunger = hunger
        self.alive = alive

    def set_position (self, pos):
        self.position = pos

    def get_position (self):
        return self.position

    def move (self):
        pass

    def eat ():
        pass