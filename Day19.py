turnsMatrix = (((1, 0, 0), (0, 1, 0), (0, 0, 1)),
               ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
               ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
               ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
               ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
               ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
               ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
               ((0, 1, 0), (1, 0, 0), (0, 0, -1)),

               ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
               ((0, 0, -1), (-1, 0, 0), (0, 1, 0)),
               ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),
               ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
               ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
               ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
               ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
               ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),

               ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
               ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
               ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
               ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
               ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
               ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
               ((0, 0, -1), (0, -1, 0), (-1, 0, 0)),
               ((0, 1, 0), (0, 0, -1), (-1, 0, 0)))

#turnsMatrix = (((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
#               ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
#               ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
#               ((0, 1, 0), (1, 0, 0), (0, 0, -1)))

def getRotatedBulk(src, turnsMults):
    res = set()
    for a in src:
        res.add((a[0] * turnsMults[0][0] + a[1] * turnsMults[0][1] + a[2] * turnsMults[0][2],
                a[0] * turnsMults[1][0] + a[1] * turnsMults[1][1] + a[2] * turnsMults[1][2],
                a[0] * turnsMults[2][0] + a[1] * turnsMults[2][1] + a[2] * turnsMults[2][2]))
    return res

def getRotatedSingle(a, turnsMults):
    return (a[0] * turnsMults[0][0] + a[1] * turnsMults[0][1] + a[2] * turnsMults[0][2],
             a[0] * turnsMults[1][0] + a[1] * turnsMults[1][1] + a[2] * turnsMults[1][2],
             a[0] * turnsMults[2][0] + a[1] * turnsMults[2][1] + a[2] * turnsMults[2][2])


def getDoubleRotation(a, b):
    res = ((a[0][0]*b[0][0] + a[1][0]*b[0][1] + a[2][0]*b[0][2],
           a[0][1]*b[0][0] + a[1][1]*b[0][1] + a[2][1]*b[0][2],
            a[0][2]*b[0][0] + a[1][2]*b[0][1] + a[2][2]*b[0][2]),

           (a[0][0]*b[1][0] + a[1][0]*b[1][1] + a[2][0]*b[1][2],
            a[0][1]*b[1][0] + a[1][1]*b[1][1] + a[2][1]*b[1][2],
            a[0][2]*b[1][0] + a[1][2]*b[1][1] + a[2][2]*b[1][2]),

           (a[0][0]*b[2][0] + a[1][0]*b[2][1] + a[2][0]*b[2][2],
            a[0][1]*b[2][0] + a[1][1]*b[2][1] + a[2][1]*b[2][2],
            a[0][2]*b[2][0] + a[1][2]*b[2][1] + a[2][2]*b[2][2]))
    return res


def checkTwelveMatches(s1, offset, s2):
    matches = 0
    for a in s1:
        cand = (a[0] - offset[0], a[1] - offset[1], a[2] - offset[2])
        if cand in s2:
            matches += 1
            if matches == 12:
                return True
    return False


def tryMatch(s1, s2):
    for turns in turnsMatrix:
        rs2 = getRotatedBulk(s2, turns)
        for b1 in s1:
            for b2 in rs2:
                offset = (b1[0] - b2[0], b1[1] - b2[1], b1[2] - b2[2])
                #print("potential offset: ", offset)
                res = checkTwelveMatches(s1, offset, rs2)
                if res:
                    #print("Found 12 matches with offset ", offset)
                    #print("Turns: ", turns)
                    return offset, turns
    return None


def main():
    data = open("resources/day19_input.txt").read().splitlines()
    sNum = 0
    scanData = {}
    scanData[sNum] = set()
    for d in data:
        if d == "":
            sNum += 1
            scanData[sNum] = set()
            continue
        if len(d) > 3 and d[0: 3] == "---":
            continue
        ds = d.split(",")
        scanData[sNum].add((int(ds[0]), int(ds[1]), int(ds[2])))
    for s in scanData:
        print(s, ": ", scanData[s])
    # take 2nd set and rotate it in every possible way
    # for each rotation, take 1st point in 0 and assume it matches every point in 1 one by one
    # for each check, calculate offset and run verification: orig 0 - offset = rotated 1  for at least 21 points
    solvedSensors = {0: ((0, 0, 0), ((1, 0, 0), (0, 1, 0), (0, 0, 1)))}
    tried = set()
    while len(solvedSensors) < len(scanData):
        newSolvedSensors = {}
        for s1 in solvedSensors:
            for s2 in scanData:
                if s1 == s2 or (s1, s2) in tried or (s2, s1) in tried or s2 in solvedSensors or s2 in newSolvedSensors:
                    continue
                tried.add((s1, s2))
                res = tryMatch(scanData[s1], scanData[s2])
                if res is not None:
                    print("Match: ", s2, " to ", s1)
                    rto0 = getDoubleRotation(res[1], solvedSensors[s1][1])
                    pto0 = getRotatedSingle(res[0], solvedSensors[s1][1])
                    pos = (pto0[0] + solvedSensors[s1][0][0], pto0[1] + solvedSensors[s1][0][1], pto0[2] + solvedSensors[s1][0][2])
                    newSolvedSensors[s2] = (pos, rto0)
                    print("Result sensor ", s2, ": ", newSolvedSensors[s2])
        for ns in newSolvedSensors:
            solvedSensors[ns] = newSolvedSensors[ns]
    #calculate full array
    allBeacons = set()
    for sensor in scanData:
        for b in scanData[sensor]:
            posR = getRotatedSingle(b, solvedSensors[sensor][1])
            posto0 = (posR[0] + solvedSensors[sensor][0][0], posR[1] + solvedSensors[sensor][0][1], posR[2] + solvedSensors[sensor][0][2])
            allBeacons.add(posto0)
    print("Number of beacons: ", len(allBeacons))
    maxDist = None
    for s1 in solvedSensors:
        for s2 in solvedSensors:
            if s2 <= s1:
                continue
            mDist = abs(solvedSensors[s1][0][0] - solvedSensors[s2][0][0]) \
                    + abs(solvedSensors[s1][0][1] - solvedSensors[s2][0][1]) \
                    + abs(solvedSensors[s1][0][2] - solvedSensors[s2][0][2])
            if maxDist is None or mDist > maxDist:
                maxDist = mDist
    print("Maximim distance: ", maxDist)


if __name__ == "__main__":
    main()
