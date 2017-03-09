import numpy as np

class Environment(object):
    """TODO: documentation"""
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.gazelle_COM
        
    def set_gazelle_COM(self, gazelles):
        vec_pos=np.array([])
        for g in gazelles:
            vec_pos = np.concatenate((vec_pos, g.position))
        
        vec_pos = vec_pos.reshape(len(gazelles)/2,2).transpose()
                
        
        self.gazelle_COM = np.floor(np.average(vec_pos,axis=0))
         
        

    def map_positions (self, lions, gazelles):
        area = []
        for l in lions:
            pos = l.position
            area[0] = pos[0]-l.radius
            area[1] = pos[0]+l.radius
            area[2] = pos[1]-l.radius
            area[3] = pos[1]+l.radius
            for k, g in enumerate(gazelles):
                if g.position[0] >= area[0] and g.position[0] <= area[1] and \
                g.position[1] >= area[2] and g.position[1] <= area[3]:
                    """TODO: obtimizar con distancia 1"""
                    l.add_targets(k)
                    
                    


