from math import sin, cos
import numpy as np
import quaternion
from random import randint

class Quadrilateral:
    @staticmethod
    def __multiplyMatricies(point, matrix):
        return np.matmul(matrix, point)

    @staticmethod
    def __zwRotation(angle, point):
        zwAxisRotation=np.array([
            [cos(angle), -sin(angle), 0, 0],
            [sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        return Quadrilateral.__multiplyMatricies(point, zwAxisRotation)

    @staticmethod
    def __ywRotation(angle, point):
        ywAxisRotation=np.array([
            [cos(angle), 0, -sin(angle), 0],
            [0, 1, 0, 0],
            [sin(angle), 0, cos(angle), 0],
            [0, 0, 0, 1]
        ])

        return Quadrilateral.__multiplyMatricies(point, ywAxisRotation)

    @staticmethod
    def __yzRotation(angle, point):
        yzAxisRotation=np.array([
            [cos(angle), 0, 0, -sin(angle)],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [sin(angle), 0, 0, cos(angle)]
        ])

        return Quadrilateral.__multiplyMatricies(point, yzAxisRotation)

    @staticmethod
    def __xwRotation(angle, point):
        xwAxisRotation=np.array([
            [1, 0, 0, 0],
            [0, cos(angle), -sin(angle), 0],
            [0, sin(angle), cos(angle), 0],
            [0, 0, 0, 1]
        ])

        return Quadrilateral.__multiplyMatricies(point, xwAxisRotation)

    @staticmethod
    def __xzRotation(angle, point):
        xzAxisRotation=np.array([
            [1, 0, 0, 0],
            [0, cos(angle), 0, -sin(angle)],
            [0, 0, 1, 0],
            [0, sin(angle), 0, cos(angle)]
        ])

        return Quadrilateral.__multiplyMatricies(point, xzAxisRotation)

    @staticmethod
    def __xyRotation(angle, point):
        xyAxisRotation=np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, cos(angle), -sin(angle)],
            [0, 0, sin(angle), cos(angle)]
        ])

        return Quadrilateral.__multiplyMatricies(point, xyAxisRotation)

    @staticmethod
    def randomRotation(quaternion, angleList): #random is T/F; order is list from 0 to 5 detailing the order of rotations
        W, X, Y, Z= quaternion.w, quaternion.x, quaternion.y, quaternion.z
        matrix=np.matrix('W; X; Y; Z')

        matrix=Quadrilateral.__zwRotation(angleList[0], matrix)
        matrix=Quadrilateral.__ywRotation(angleList[1], matrix)
        matrix=Quadrilateral.__yzRotation(angleList[2], matrix)
        matrix=Quadrilateral.__xwRotation(angleList[3], matrix)
        matrix=Quadrilateral.__xzRotation(angleList[4], matrix)
        matrix=Quadrilateral.__xyRotation(angleList[5], matrix)

        W, X, Y, Z=matrix[0], matrix[1], matrix[2], matrix[3]
        return np.quaternion(W, X, Y, Z)