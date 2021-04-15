from fractal import *
from helpers import *

import quaternion
import numpy as np

class Mesh:
    @staticmethod
    def __calcFractalIntersect(pos, vel, n, t):
        # TODO: Improve algorythm
        for _ in range(floor(n+1)):
            if Fractal.calcFractal( pos, t )[0] == True:
                return pos
            
            pos += vel
        
        return pos

    @staticmethod
    def __calcPixel(x, y, pos, t):
        # TODO: Rotate
        vec = np.quaternion( x, y, FORWARD_AMOUNT, 0 )

        mag = abs(vec)/VECTOR_MAGNITUDE_CHANGE
        vec /= 1 if mag == 0 else mag

        res = Mesh.__calcFractalIntersect( 
            pos.copy(), 
            vec, 
            MAX_FRACTAL_SEARCH_DIST//VECTOR_MAGNITUDE_CHANGE, 
            t
        )

        return res

    @staticmethod
    def calcFrame( t ):
        firstIntersect = np.ndarray(( WIDTH, HEIGHT ), dtype=np.quaternion)

        pos = FT(t)

        for x in range(0, WIDTH):
            print(t/(VIDEO_TIME*FPS ), x/WIDTH)
            for y in range(0, HEIGHT):
                firstIntersect[x][y] = Mesh.__calcPixel( x - WIDTH//2, y - HEIGHT // 2, pos, t)
    

        return firstIntersect

        