from math import *
import numpy as np
import quaternion
from random import randint

class Quadrilateral:
    @staticmethod
    def __multiplyMatricies(point1, point2, point3, point4, matrix):
        return np.matmul(matrix, point1), np.matmul(matrix, point2), np.matmul(matrix, point3), np.matmul(matrix, point4)

    @staticmethod
    def __zwRotation(angle, point1, point2, point3, point4):
        zwAxisRotation=np.array([
            [cos(angle), -sin(angle), 0, 0],
            [sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        return Quadrilateral.__multiplyMatricies(point1, point2, point3, point4, zwAxisRotation)

    @staticmethod
    def __ywRotation(angle, point1, point2, point3, point4):
        ywAxisRotation=np.array([
            [cos(angle), 0, -sin(angle), 0],
            [0, 1, 0, 0],
            [sin(angle), 0, cos(angle), 0],
            [0, 0, 0, 1]
        ])

        return Quadrilateral.__multiplyMatricies(point1, point2, point3, point4, ywAxisRotation)

    @staticmethod
    def __yzRotation(angle, point1, point2, point3, point4):
        yzAxisRotation=np.array([
            [cos(angle), 0, 0, -sin(angle)],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [sin(angle), 0, 0, cos(angle)]
        ])

        return Quadrilateral.__multiplyMatricies(point1, point2, point3, point4, yzAxisRotation)

    @staticmethod
    def __xwRotation(angle, point1, point2, point3, point4):
        xwAxisRotation=np.array([
            [1, 0, 0, 0],
            [0, cos(angle), -sin(angle), 0],
            [0, sin(angle), cos(angle), 0],
            [0, 0, 0, 1]
        ])

        return Quadrilateral.__multiplyMatricies(point1, point2, point3, point4, xwAxisRotation)

    @staticmethod
    def __xzRotation(angle, point1, point2, point3, point4):
        xzAxisRotation=np.array([
            [1, 0, 0, 0],
            [0, cos(angle), 0, -sin(angle)],
            [0, 0, 1, 0],
            [0, sin(angle), 0, cos(angle)]
        ])

        return Quadrilateral.__multiplyMatricies(point1, point2, point3, point4, xzAxisRotation)

    @staticmethod
    def __xyRotation(angle, point1, point2, point3, point4):
        xyAxisRotation=np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, cos(angle), -sin(angle)],
            [0, 0, sin(angle), cos(angle)]
        ])

        return Quadrilateral.__multiplyMatricies(point1, point2, point3, point4, xyAxisRotation)

    @staticmethod
    def randomRotation(quaternion, angleList, random, order): #random is T/F; order is list from 0 to 5 detailing the order of rotations
        W, X, Y, Z= quaternion.w, quaternion.x, quaternion.y, quaternion.z

        if random:
            randomNumber=random.randint(0, 5)

            if randomNumber==0:
                W, X, Y, Z= Quadrilateral.__zwRotation(angleList[0], W, X, Y, Z)
            if randomNumber==1:
                W, X, Y, Z= Quadrilateral.__ywRotation(angleList[1], W, X, Y, Z)
            if randomNumber==2:
                W, X, Y, Z= Quadrilateral.__yzRotation(angleList[2], W, X, Y, Z)
            if randomNumber==3:
                W, X, Y, Z= Quadrilateral.__xwRotation(angleList[3], W, X, Y, Z)
            if randomNumber==4:
                W, X, Y, Z= Quadrilateral.__xzRotation(angleList[4], W, X, Y, Z)
            if randomNumber==5:
                W, X, Y, Z= Quadrilateral.__xyRotation(angleList[5], W, X, Y, Z)
        else:
            for whichRotation in order:
                if whichRotation==0:
                    W, X, Y, Z= Quadrilateral.__zwRotation(angleList[0], W, X, Y, Z)
                if whichRotation==1:
                    W, X, Y, Z= Quadrilateral.__ywRotation(angleList[1], W, X, Y, Z)
                if whichRotation==2:
                    W, X, Y, Z= Quadrilateral.__yzRotation(angleList[2], W, X, Y, Z)
                if whichRotation==3:
                    W, X, Y, Z= Quadrilateral.__xwRotation(angleList[3], W, X, Y, Z)
                if whichRotation==4:
                    W, X, Y, Z= Quadrilateral.__xzRotation(angleList[4], W, X, Y, Z)
                if whichRotation==5:
                    W, X, Y, Z= Quadrilateral.__xyRotation(angleList[5], W, X, Y, Z)

        return np.quaternion(W, X, Y, Z)
