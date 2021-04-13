from fractal import *

class Mesh:
    @staticmethod
    def __calcFractalIntersect(pos, vel, n, t):
        for i in range(n):
            if Fractal.calcFractal( pos, t )[0] == True:
                return pos
            
            pos += vel
        
        return pos

    @staticmethod
    def __calcPixel(x, y, pos, t):
        # TODO: Rotate
        vec = np.quaternion( x, y, 0, 0 )
        mag = abs(vec)/VECTOR_MAGNITUDE_CHANGE
        vec /= 1 if mag == 0 else mag

        res = Mesh.__calcFractalIntersect( 
            pos.copy(), 
            vec, 
            MAX_FRACTAL_SEARCH_DIST//VECTOR_MAGNITUDE_CHANGE, 
            t 
        )


        if round(Fractal.dist( res, pos )*10000) == round(MAX_FRACTAL_SEARCH_DIST*10000): # May cause error due to epsilon
            return np.array( [0, 0, 0] ) 
        else:
            dist = Fractal.dist( pos, res )

            return np.array([ 255*dist//MAX_FRACTAL_SEARCH_DIST, 0, 255])
        

    @staticmethod
    def calcFrame( t ):
        image = np.ndarray(
            ( WIDTH, HEIGHT, 3 )
        )

        pos = FT(t)

        for x in range(0, WIDTH):
            print(x/WIDTH)
            for y in range(0, HEIGHT):
                image[x][y][0:3] = Mesh.__calcPixel( x - WIDTH//2, y - HEIGHT // 2, pos, t)[0:3]
        
        return image

        