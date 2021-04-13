from mesh import *
from matplotlib import pyplot as plt

from fractal import *

'''
TODO: Multithread
'''

if __name__ == "__main__":
    # 1) Get settings file to use from user
    # 2) For each frame
        # 3) generate mesh
        # 4) plot and save mesh
    # 5) Convert to video
    
    # Generates the mesh
    image = Mesh.calcFrame( 0 )
    plt.imshow( image )
    plt.show()
    
    # X, Y, Z = [], [], []
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')

    # r = 20
    # for x in range(-r, r):
    #     for y in range(-r, r):
    #         for z in range(-r, r):
    #             if Fractal.calcFractal( np.quaternion(x/20, y/20, z/20), 0 )[0] == True:
    #                 X.append(x)
    #                 Y.append(y)
    #                 Z.append(z)
    
    # ax.scatter(X, Y, Z)
    # plt.show()
