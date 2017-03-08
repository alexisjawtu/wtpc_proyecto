class Environment(object):
    """TODO: documentation"""
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def map_positions (self, lions, gazelles):
        for l in lions:
            pos = l.position
            area[0] = pos[0]-l.radius
            area[1] = pos[0]+l.radius
            area[2] = pos[1]-l.radius
            area[3] = pos[1]+l.radius
            for g in gazelles:
                if g.position[0] >= area[0] and g.position[0] <= area[1]:
                    pass
