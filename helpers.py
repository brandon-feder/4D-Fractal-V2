import quaternion
import numpy as np

from math import *

class Helpers:
    @staticmethod
    def dist(A, B=np.quaternion(0, 0, 0, 0)):
        return abs(A - B)