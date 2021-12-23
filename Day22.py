X = "x"
Y = "y"
Z = "z"
INC = "inc"

def printLitCubes(cubes):
    print("==== LIT CUBES ====")
    numDots = 0
    for c in cubes:
#        print(c)
        numDots += (c[X][1]-c[X][0]+1) * (c[Y][1]-c[Y][0]+1) * (c[Z][1]-c[Z][0]+1)
    print("Total lit dots: ", numDots)

def getOutsidePart(oldCube, newCube):
    #print("Get outside part:")
    #print(oldCube)
    #print(newCube)
    if newCube[X][0] > oldCube[X][1] or newCube[X][1] < oldCube[X][0] or \
            newCube[Y][0] > oldCube[Y][1] or newCube[Y][1] < oldCube[Y][0] or \
            newCube[Z][0] > oldCube[Z][1] or newCube[Z][1] < oldCube[Z][0]:
        return [newCube]
    newCubes = [{X: (newCube[X][0], newCube[X][1]),
                 Y: (newCube[Y][0], newCube[Y][1]),
                 Z: (newCube[Z][0], newCube[Z][1]),
                 INC: True}]
    for c in (X, Y, Z):
        remCubes = []
        for nc in newCubes:
            if not nc[INC] or nc[c][0] > oldCube[c][1] or nc[c][1] < oldCube[c][0]:
                nc[INC] = False
                remCubes.append(nc)
            elif nc[c][0] >= oldCube[c][0] and nc[c][1] <= oldCube[c][1]:
                remCubes.append(nc)
            else:
                c1 = None
                c2 = None
                c3 = {}
                if nc[c][0] < oldCube[c][0]:
                    c1 = {}
                    for coord in (X, Y, Z):
                        if coord != c:
                            c1[coord] = nc[coord]
                        else:
                            c1[coord] = (nc[coord][0], oldCube[coord][0]-1)
                    c1[INC] = False

                if nc[c][1] > oldCube[c][1]:
                    c2 = {}
                    for coord in (X, Y, Z):
                        if coord != c:
                            c2[coord] = nc[coord]
                        else:
                            c2[coord] = (oldCube[coord][1]+1, nc[coord][1])
                    c2[INC] = False
                for coord in (X, Y, Z):
                    if coord != c:
                        c3[coord] = nc[coord]
                    else:
                        c3[coord] = (max(nc[coord][0], oldCube[coord][0]), min(nc[coord][1], oldCube[coord][1]))
                    c3[INC] = True
                if c1 is not None:
                    remCubes.append(c1)
                if c2 is not None:
                    remCubes.append(c2)
                remCubes.append(c3)
        newCubes = remCubes
        #print("After processing ", c)
        #print(newCubes)
    res = []
    for cube in newCubes:
        if not cube[INC]:
            res.append({X: cube[X], Y: cube[Y], Z: cube[Z]})
    return res


def addAndProcessCube(cubes, cube, turnOn):
    if turnOn:
        newCubes = [cube]
        for c in cubes:
            toAdd = []
            for nc in newCubes:
                nnc = getOutsidePart(c, nc)
                toAdd += nnc
            newCubes = toAdd
        for nc in newCubes:
            cubes.append(nc)
    else:
        newCubes = []
        for c in cubes:
            nnc = getOutsidePart(cube, c)
            newCubes += nnc
        cubes.clear()
        cubes += newCubes


def truncateCube(cube, minValue, maxValue):
    for c in (X, Y, Z):
        cube[c] = (max(cube[c][0], minValue), min(cube[c][1], maxValue))
        if cube[c][0] > cube[c][1]:
            return None
    return cube


def main():
    data = open("resources/day22_input.txt").read().splitlines()
    cubes = []
    for d in data:
        ds = d.split()
        dss = ds[1].split(",")
        dx = dss[0][2:].split("..")
        x1 = int(dx[0])
        x2 = int(dx[1])
        dy = dss[1][2:].split("..")
        y1 = int(dy[0])
        y2 = int(dy[1])
        dz = dss[2][2:].split("..")
        z1 = int(dz[0])
        z2 = int(dz[1])
        cube = {X: (x1, x2), Y: (y1, y2), Z: (z1, z2)}
        #cube = truncateCube(cube, -50, 50)
        print("Adding ", ds[0], cube, "total ", len(cubes), " cubes")
        if cube is not None:
            addAndProcessCube(cubes, cube, ds[0] == "on")
    printLitCubes(cubes)





if __name__ == "__main__":
    main()
