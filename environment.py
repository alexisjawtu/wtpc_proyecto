import numpy as np
from lion import Lion
from gazelle import Gazelle

class Environment(object):
    """TODO: documentation"""
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def set_width(self,width):
        self.width = width
        
    def set_height(self, height):
        self.height = height    
        

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
                if g.get_alive() and (p[0] >= area[0]) and (p[0] <= area[1]) and \
                (p[1] >= area[2]) and (p[1] <= area[3]):
                    """TODO: optimizar con distancia 1"""
                    l.add_target(k)
    
    def herd_lion(self, num_lion, stepLion, hungerLion, radLion, probAt):
        lions = []
        for p in range(num_lion):
            x = np.random.randint(int(self.width*0.375),int(self.width*0.625))
            y = np.random.randint(int(self.height*0.375),int(self.height*0.625))
            PosL = np.array([x, y])
            
            stepL = stepLion + np.random.randint(-1,1)
            hungerL = np.random.normal(hungerLion,3)
            radL = int(np.random.normal(radLion,3))
            probL = max(np.random.normal(probAt,0.03),1)

            lions.append(Lion(PosL, stepL, hungerL, radL, probL))
        return lions

    def herd_gazelle(self, num_gaz, gazelle_mass, stepG, hungerG):
        gazelles = []
        for p in range(num_gaz):
            x = np.random.randint(int(self.width*0.125),int(self.width*0.875))
            y = np.random.randint(int(self.height*0.125),int(self.height*0.875))
            PosGaz = np.array([x, y])
            hungerG = np.random.normal(hungerG,3)
            gazelles.append(Gazelle(PosGaz, gazelle_mass, stepG, hungerG))
        return gazelles