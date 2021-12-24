import copy

A = 'A'
B = 'B'
C = 'C'
D = 'D'
H = 'H'
AMPHIPODS = 'AMP'
BURROWS = "BUR"
HALLWAY = 'HAL'
BPOS = {A: 2, B: 4, C: 6, D: 8}
VALIDHALLWAYPOS = (0, 1, 3, 5, 7, 9, 10)
MOVECOSTS = {A: 1, B: 10, C: 100, D: 1000}

NUMLEVELS = 4

bestscore = None

def printMap(data):
    print("#############")
    s = "#"
    pos = 0
    while pos <= 10:
        if pos not in VALIDHALLWAYPOS:
            s += "."
        else:
            if data[HALLWAY][pos] is None:
                s += "."
            else:
                s += data[HALLWAY][pos]
        pos += 1
    s += "#"
    print(s)
    for i in range(NUMLEVELS):
        s = "###" if i == 0 else "  #"
        for p in (A, B, C, D):
            if data[BURROWS][p][NUMLEVELS - 1 - i] is None:
                s += "."
            else:
                s += data[BURROWS][p][NUMLEVELS - 1 - i]
            s += "#"
        if i == 0:
            s += "##"
        print(s)
    print("  #########")



def moveTo(a, newloc, newpos, data):
    am = data[AMPHIPODS][a]
    if am[1] == H:
        data[HALLWAY][am[2]] = None
    else:
        data[BURROWS][am[1]][am[2]] = None
    am = (am[0], newloc, newpos)
    data[AMPHIPODS][a] = am
    if newloc == H:
        data[HALLWAY][newpos] = am[0]
    else:
        data[BURROWS][newloc][newpos] = am[0]


def getPossibleMoves(a, data):
    am = data[AMPHIPODS][a]
    if am[1] != H:
        # check of there are archs above in burrow
        if am[2] < NUMLEVELS-1:
            for i in range(am[2]+1, NUMLEVELS):
                if data[BURROWS][am[1]][i] is not None:
                    return []
        if am[1] == am[0]:
            inplace = True
            for i in range(am[2]):
                if data[BURROWS][am[1]][i] is not None and data[BURROWS][am[1]][i] != am[0]:
                    inplace = False
                    break
            if inplace:
                return []
        res = []
        pos = BPOS[am[1]]
        while pos < 10:
            pos += 1
            if pos == BPOS[am[0]]:
                bur = data[BURROWS][am[0]]
                depth = 0
                while depth < NUMLEVELS:
                    if bur[depth] is None:
                        break
                    if bur[depth] != am[0]:
                        depth = None
                        break
                    depth += 1
                if depth is not None:
                    res.append((am[0], depth, getRouteCost(am[0], am[1], am[2], am[0], depth)))
            if pos not in VALIDHALLWAYPOS:
                pos += 1
            if data[HALLWAY][pos] is None:
                res.append((H, pos, getRouteCost(am[0], am[1], am[2], H, pos)))
            else:
                break
        pos = BPOS[am[1]]
        while pos > 0:
            pos -= 1
            if pos == BPOS[am[0]]:
                bur = data[BURROWS][am[0]]
                depth = 0
                while depth < NUMLEVELS:
                    if bur[depth] is None:
                        break
                    if bur[depth] != am[0]:
                        depth = None
                        break
                    depth += 1
                if depth is not None:
                    res.append((am[0], depth, getRouteCost(am[0], am[1], am[2], am[0], depth)))
            if pos not in VALIDHALLWAYPOS:
                pos -= 1
            if data[HALLWAY][pos] is None:
                res.append((H, pos, getRouteCost(am[0], am[1], am[2], H, pos)))
            else:
                break
        return res
    else:  # amphipod is in the hallway
        bur = data[BURROWS][am[0]]
        pos = am[2]
        while pos != BPOS[am[0]]:
            pos += 1 if pos < BPOS[am[0]] else -1
            if pos in VALIDHALLWAYPOS:
                if data[HALLWAY][pos] is not None:
                    return []

        depth = 0
        while depth < NUMLEVELS:
            if bur[depth] is None:
                break
            if bur[depth] != am[0]:
                depth = None
                break
            depth += 1
        if depth is not None:
            res = [(am[0], depth, getRouteCost(am[0], am[1], am[2], am[0], depth))]
        else:
            res = []
        return res


def getRouteCost(a, fromloc, frompos, toloc, topos):
    steps = 0
    pos = frompos
    if fromloc != H:
        steps = NUMLEVELS - frompos
        pos = BPOS[fromloc]
    dpos = topos if toloc == H else BPOS[toloc]
    steps += abs(dpos - pos)
    if toloc != H:
        steps += NUMLEVELS - topos
    return steps * MOVECOSTS[a]

def checkWin(data):
    for a in (A, B, C, D):
        for i in range(NUMLEVELS):
            if data[BURROWS][a][i] is None or data[BURROWS][a][i] != a:
                return False
    return True


def getHash(data):
    s = ""
    for i in VALIDHALLWAYPOS:
        s += '.' if data[HALLWAY][i] is None else data[HALLWAY][i]
    for i in (A, B, C, D):
        for j in range(NUMLEVELS):
            s += '.' if data[BURROWS][i][j] is None else data[BURROWS][i][j]
    return s

def solve(data, cache, cost):
    global bestscore
    if checkWin(data):
        if bestscore is None or cost < bestscore:
            bestscore = cost
            print("Solved, cost = ", cost)
        return
    hash = getHash(data)
    if hash in cache and cache[hash] <= cost:
        return
    else:
        cache[hash] = cost
    for a in data[AMPHIPODS]:
        moves = getPossibleMoves(a, data)
        for m in moves:
            newData = copyData(data)
            moveTo(a, m[0], m[1], newData)
            solve(newData, cache, cost + m[2])

def copyData(data):
    amphipods = {'A1': data[AMPHIPODS]['A1'], 'A2': data[AMPHIPODS]['A2'],
                 'B1': data[AMPHIPODS]['B1'], 'B2': data[AMPHIPODS]['B2'],
                 'C1': data[AMPHIPODS]['C1'], 'C2': data[AMPHIPODS]['C2'],
                 'D1': data[AMPHIPODS]['D1'], 'D2': data[AMPHIPODS]['D2'],
                 'A3': data[AMPHIPODS]['A3'], 'A4': data[AMPHIPODS]['A4'],
                 'B3': data[AMPHIPODS]['B3'], 'B4': data[AMPHIPODS]['B4'],
                 'C3': data[AMPHIPODS]['C3'], 'C4': data[AMPHIPODS]['C4'],
                 'D3': data[AMPHIPODS]['D3'], 'D4': data[AMPHIPODS]['D4']}
    burrows = {}
    for p in (A, B, C, D):
        burrows[p] = []
        for i in range(NUMLEVELS):
            burrows[p].append(data[BURROWS][p][i])
    hallway = {}
    for p in VALIDHALLWAYPOS:
        hallway[p] = data[HALLWAY][p]
    return {AMPHIPODS: amphipods, BURROWS: burrows, HALLWAY: hallway}

def calculateAmphipods(burrows):
    counter = {A: 1, B: 1, C: 1, D: 1}
    amphipods = {}
    for a in (A, B, C, D):
        for i in range(NUMLEVELS):
            s = burrows[a][i] + str(counter[burrows[a][i]])
            counter[burrows[a][i]] += 1
            amphipods[s] = (burrows[a][i], a, i)
    return amphipods


def main():
    # --- TEST ---
    #burrows = {A: [A, D, D, B], B: [D, B, C, C], C: [C, A, B, B], D: [A, C, A, D]}

    # --- PROD ---
    burrows = {A: [C, D, D, C], B: [A, B, C, A], C: [D, A, B, B], D: [B, C, A, D]}
    amphipods = calculateAmphipods(burrows)

    hallway = {0: None, 1: None, 3: None, 5: None, 7: None, 9: None, 10: None}
    data = {AMPHIPODS: amphipods, BURROWS: burrows, HALLWAY: hallway}
    printMap(data)

    solve(data, {}, 0)
    print(bestscore)


if __name__ == '__main__':
    main()
