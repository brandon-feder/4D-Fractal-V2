import quaternion
import numpy as np

from math import *

'''
The maximum iteration deapth used when calculating the fractal
'''
MAX_DEPTH = 25

'''
The radious that define when a Z has escaped to far enough not to be in the set
'''
ESCAPE_RADIOUS = 4

'''
The distance that the "camera" is from the screen
'''
CAMERA_DIST = 10

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
Change in angle in both directions
'''
D_ANGLE = 0.0005


'''
The rate of change of the vector
'''
VECTOR_MAGNITUDE_CHANGE = 1

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
    return Z*Z + variables[0], variables

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
    return np.quaternion( -CAMERA_DIST, 0, 0, 0 )


