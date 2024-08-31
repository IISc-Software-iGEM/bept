from functools import lru_cache

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
@lru_cache(maxsize=None)
def extract(filepath, return_data=False):
    """
# Data from APBS 3.4.1
#
# POTENTIAL (kT/e)
#
object 1 class gridpositions counts 353 193 257
origin 6.617750e+01 9.325490e+01 7.383950e+01
delta 4.895710e-01 0.000000e+00 0.000000e+00
delta 0.000000e+00 4.995792e-01 0.000000e+00
delta 0.000000e+00 0.000000e+00 4.786953e-01
object 2 class gridconnections counts 353 193 257
object 3 class array type double rank 0 items 17509153         data follows
8.841046e-01 8.803156e-01 8.765030e-01
8.726683e-01 8.688033e-01 8.649116e-01
8.610003e-01 8.570672e-01 8.531058e-01
8.491277e-01 8.451333e-01 8.411144e-01
...
This is the general format, where first potential is of the format 
U(0,0,0) U(0,0,1) U(0,0,2)
U(0,0,3) U(0,0,4) U(0,0,5)
...

    The function reads the file and extracts the potential data at (i,j,k)
    """
    # Read the data
    with open(filepath) as f:
        data = f.readlines()

    nx,ny,nz = 0,0,0 # grid box size
    xmin, ymin, zmin = 0,0,0 # origin
    ind, end=0, 0 # start and end of the potential data
    hx, hy, hz = 0,0,0 # grid spacing length
    # Extract length, width, height as nx, ny, nz
    for line in data:
        ind+=1
        if line.startswith('origin'):
            origin= line.split()
            xmin = float(origin[1]) 
            ymin = float(origin[2]) 
            zmin = float(origin[3]) 
        elif line.startswith('delta'):
            delta= line.split()
            hx = float(delta[1]) if hx==0 else hx
            hy = float(delta[2]) if hy==0 else hy
            hz = float(delta[3]) if hz==0 else hz
        elif line.startswith('object 3'):
            break
        elif line.startswith('object 1'):
            line= line.split()
            for i in range(len(line)):
                try:
                    if int(line[i]) and int(line[i]):
                        nx = int(line[i])
                        ny = int(line[i+1])
                        nz = int(line[i+2])
                        break
                except:
                    pass

    # print("grid box: ", nx,ny,nz)
    # print("grid spacing: ", hx, hy, hz)
    # print("min: ", xmin, ymin, zmin)

    pot_data = data[ind:]

    if return_data == True:
        return xmin, ymin, zmin, hx, hy, hz, nx, ny, nz, pot_data
    else:
        return xmin, ymin, zmin, hx, hy, hz, nx, ny, nz