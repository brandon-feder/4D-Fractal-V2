from mesh import *
from matplotlib import pyplot as plt

from fractal import *
from color import *
from settings import *
import os

'''
TODO: Multithread
'''

def saveFrame(t):
    distances = Mesh.calcFrame(t)
    image = Color.colorDist(distances, t) 

    plt.imshow(image)
    plt.savefig("./data/{}.png".format(t))

def debugOption1(t):
    X, Y, Z = [], [], []
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    r = 20
    for x in range(-r, r):
        for y in range(-r, r):
            for z in range(-r, r):
                if Fractal.calcFractal( np.quaternion(x/20, y/20, z/20), 0 )[0] == True:
                    X.append(x)
                    Y.append(y)
                    Z.append(z)
    
    ax.scatter(X, Y, Z)
    plt.show()

if __name__ == "__main__":
    # 1) Get settings file to use from user
    # 2) For each frame
        # 3) generate mesh
        # 4) plot and save mesh
    # 5) Convert to video
    
    # Generates the mesh
    for t in range(VIDEO_TIME * FPS):
        saveFrame(t)
    
    os.system("rm ./{}.mov; ffmpeg -framerate {} -start_number 0 -i ./data/%d.png {}.mov".format(VIDEO_NAME, FPS, VIDEO_NAME))
    
    # debugOption1(0)
