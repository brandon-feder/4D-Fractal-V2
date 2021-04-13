import quaternion
import numpy as np
from math import *

from settings import *

class Fractal:
    @staticmethod
    def dist(A, B=np.quaternion(0, 0, 0, 0)):
        return sqrt( 
            (A.w - B.w)**2 +  
            (A.x - B.x)**2 + 
            (A.y - B.y)**2 + 
            (A.z - B.z)**2
        )

    '''
    Does the calculation of the fractal given the position and time
    '''
    @staticmethod
    def calcFractal(pos, t):
        # TODO: Rotate and translate pos
        Z, variables = F1( pos, [], t )

        info = {
            "orbit":[ Z ]
        }

        for _ in range(MAX_DEPTH):
            if Fractal.dist( Z ) > ESCAPE_RADIOUS:
                return False, info

            Z, variables = FN(Z, variables, t)

            info["orbit"].append(Z)
        
        return True, info
    