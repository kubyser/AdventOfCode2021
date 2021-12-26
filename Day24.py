W = 'w'
X = 'x'
Y = 'y'
Z = 'z'

registry = {W: 0, X: 0, Y: 0, Z: 0}
cache = set()

#DIGITS = ('9', '8', '7', '6', '5', '4', '3', '2', '1')
DIGITS = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

REQUIREDX = {0: 1, 1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 1, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}

def clearRegistry():
    global registry
    for r in (W, X, Y, Z):
        registry[r] = 0


def getValue(a):
    global registry
    if a in (W, X, Y, Z):
        return registry[a]
    return int(a)

def runProgram(program, inputString):
    global registry
    inputPos = 0
    for com in program:
        com = com.split()
        if com[0] == 'inp':
            registry[com[1]] = int(inputString[inputPos])
            inputPos += 1
        elif com[0] == 'add':
            registry[com[1]] = registry[com[1]] + getValue(com[2])
        elif com[0] == 'mul':
            registry[com[1]] = registry[com[1]] * getValue(com[2])
        elif com[0] == 'div':
            registry[com[1]] = int(registry[com[1]] // getValue(com[2]))
        elif com[0] == 'mod':
            registry[com[1]] = registry[com[1]] % getValue(com[2])
        elif com[0] == 'eql':
            registry[com[1]] = 1 if registry[com[1]] == getValue(com[2]) else 0


def copyRegistry(sourceRegistry):
    return {W: sourceRegistry[W], X: sourceRegistry[X], Y: sourceRegistry[Y], Z: sourceRegistry[Z]}


def runTree(progArray, depth, num):
    global registry
    global cache
    if (depth, registry[Z]) in cache:
        return False
    z = registry[Z]
    for i in DIGITS:
        registry[Z] = z
        runProgram(progArray[depth], i)
        #print(depth, z, i, registry[Z])
        if depth == 13:
            if registry[Z] == 0:
                print(num + i)
                print(registry)
                return True
        else:
            if registry[X] == REQUIREDX[depth]:
                if runTree(progArray, depth+1, num+i):
                    return True
    cache.add((depth, z))
    return False




def main():
    global registry
    program = open("resources/day24_input.txt").read().splitlines()
    progArray = []
    for i in range(14):
        progArray.append(program[i*18: (i+1)*18])
    runTree(progArray, 0, '')

if __name__ == "__main__":
    main()



