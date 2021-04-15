from settings import *
from helpers import *

from math import *

class Color:
    @staticmethod
    def colorDist(distances, t):
        image = np.zeros( (WIDTH, HEIGHT, 3), dtype=np.uint8 )

        pos = FT(t)
        coef = 10/VECTOR_MAGNITUDE_CHANGE

        for x in range(WIDTH):
            for y in range(HEIGHT):

                res = distances[x][y]

                if round( Helpers.dist( res, pos )*coef ) < round( MAX_FRACTAL_SEARCH_DIST*coef ):
                    dx = 1 if x < WIDTH//2 else -1
                    dy = 1 if y < HEIGHT//2 else -1

                    i = distances[x][y]
                    j = distances[x+dx][y]
                    k = distances[x][y+dy]

                    ij = j - i
                    ik = k - i

                    ij_mat = np.array( [ ij.w, ij.x, ij.y, ij.z ] )
                    ik_mat = np.array( [ ik.w, ik.x, ik.y, ik.z ] )

                    norm = ij * ik

                    norm /= abs(norm)

                    switch  = abs(norm - LIGHT_SOURCE) < abs(-norm -  LIGHT_SOURCE)

                    norm *= -1 if switch else 1

                    angle = acos( ( 2 - abs( norm - LIGHT_SOURCE )**2 ) / 2 )
                    
                    # image[x][y][0:3] = np.array( [ 255*( switch ), 0, 0 ], dtype=np.uint8 )

                    intensity = log(angle/(DIFFUSE_CONSTANT*pi))**2/ log(2/DIFFUSE_CONSTANT)**2

                    image[x][y][0:3] = np.array( [255*abs( distances[x][y] - FT(t) )/MAX_FRACTAL_SEARCH_DIST, 0, 255*abs( distances[x][y] - FT(t) )/MAX_FRACTAL_SEARCH_DIST] )

                    # image[x][y][0:3] = np.array( [ 255*intensity , 0, 0 ], dtype=np.uint8 )
                else:
                    image[x][y][0:3] = np.array( [255, 255, 255], dtype=np.uint8 )
        
        return image
