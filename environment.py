import numpy as np

class Environment(object):
    """TODO: documentation"""
    def __init__ (self, width, height ):
        self.width = width
        self.height = height
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def set_width(self,width):
        self.width = width
        
    def set_height(self, heigth):
        self.width = heigth    
        

    def gazelle_COM(self, gazelles):
        """Center Of Mass of gazelles"""
        vec_pos=np.array([])
        for g in gazelles:
            vec_pos = np.concatenate((vec_pos, g.position))
        
        vec_pos = vec_pos.reshape(len(gazelles)/2,2).transpose()
       
        return np.floor(np.average(vec_pos,axis=0))
   
      
    def map_positions(self, lions, gazelles):
        """DOCUMENTAR """
        area = [0]*4
        for l in lions:
            pos = l.get_position()
            r = l.get_radius()
            area[0] = pos[0] - r
            area[1] = pos[0] + r
            area[2] = pos[1] - r
            area[3] = pos[1] + r
            
            for k, g in enumerate(gazelles):
                p = g.get_position()
                if p[0] >= area[0] and p[0] <= area[1] and \
                p[1] >= area[2] and p[1] <= area[3]:
                    """TODO: obtimizar con distancia 1"""
                    l.add_target(k)
                    
                    


