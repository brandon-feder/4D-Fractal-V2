import quaternion
import numpy as np

from helpers import *

from math import *

'''
The maximum iteration deapth used when calculating the fractal
'''
MAX_DEPTH = 25

'''
The radious that define when a Z has escaped to far enough not to be in the set
'''
ESCAPE_RADIOUS = 10

'''
The distance that the "camera" is from the screen
'''
CAMERA_DIST = 3

'''
The maximum distance away from the fractal to search for
'''
MAX_FRACTAL_SEARCH_DIST = 2*CAMERA_DIST

'''
Width and hight of canvas
'''
WIDTH = 250
HEIGHT = 250

'''
The rate of change of the vector
'''
VECTOR_MAGNITUDE_CHANGE = 0.5

'''
Weight of going foward. Related FOV
'''
FORWARD_AMOUNT = WIDTH

'''
Returns the inital variables needed in calculating the fractal

Parameters:
    - C: The coordinate of the point the initial coordinate
    - variables: A list of extra accesory variables
    - t: The the time which can optionally be used in the fractals calculation

Returns:
    - The initial values of Z
    - All the variables needed for the rest of the calculations
'''
def F1( C, variables, t ):
    return np.quaternion(0, 0, 0, 0), [C] + variables

'''
Returns the updated values ued in calculating the fractal

Parameters:
    - Z: The coordinate of the point the initial coordinate
    - variables: A list of extra accesory variables
    - t: The the time which can optionally be used in the fractals calculation

Returns:
    - The next values of Z
    - All the variables needed for the rest of the calculations
'''
def FN( Z, variables, t ):
    return Z**(1 + t/20) + variables[0], variables

    # return Z*Z + variables[0], variables

'''
Calculates the angles to rotate by

Parameters:
    - t: The time which can optionally be used to calculate the angles

Returns:
    - A list of angles used in the rotations
'''
def FR( t ):
    return 1, 2, 3, 4, 5, 6

'''
Calculates the quaternion to translate by

Parameters:
    - t: The time which can optionally be used to calculate the translation

Returns:
    - A quaternion to translate with
'''
def FT( t ):
    return np.quaternion( 0, 0, -CAMERA_DIST, 0 )

'''
Number of threads to launch
'''
N_THREADS = 8

'''
Whether to parrallelize or not
'''
PARRALLEL = True

'''
The light source position vector
'''
LIGHT_SOURCE = np.quaternion( 0, -10, -10, 0 ) # Only edit this line
LIGHT_SOURCE /= abs(LIGHT_SOURCE)

DIFFUSE_CONSTANT = 1

VIDEO_NAME, VIDEO_TIME, FPS = "video", 10, 15