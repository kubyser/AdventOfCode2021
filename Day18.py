import math

TYPE_NUMERAL = "numeral"
TYPE_PAIR = "pair"

PARENT = "parent"
ID = "id"
LEFT = "left"
RIGHT = "right"
TYPE = "type"
VALUE = "value"

DIRECTION_RIGHT = 0
DIRECTION_LEFT = 1

nextId = 0
globalTree = {}

def getNextId():
    global nextId
    nextId += 1
    return nextId-1

def nodeToStr(p):
    if p is None:
        return "NONE"
    if p[TYPE] == TYPE_NUMERAL:
        return str(p[VALUE])
    s = "["
    s += nodeToStr(p[LEFT])
    s += ", "
    s += nodeToStr(p[RIGHT])
    s += "]"
    return s


def parsePair(s, startPos, parent):
    pos = startPos + 1
    res = {ID:getNextId(), PARENT: parent[ID] if parent is not None else None, TYPE: None, LEFT: None, RIGHT: None, VALUE: None}
    globalTree[res[ID]] = res
    for i in (LEFT, RIGHT):
        if s[pos] == "[":
            res[TYPE] = TYPE_PAIR
            num, pos = parsePair(s, pos, res)
            res[i] = num
        else:
            ns = ""
            while s[pos] not in {",", "]"}:
                ns += s[pos]
                pos += 1
            res[i] = {ID: getNextId(), PARENT: res[ID], TYPE: TYPE_NUMERAL, LEFT: None, RIGHT: None, VALUE: int(ns)}
            globalTree[res[i][ID]] = res[i]
        pos += 1
    return res, pos


def parseNum(s):
    return parsePair(s, 0, None)[0]


def findPairToExplode(root, startDepth):
    if root[TYPE] == TYPE_NUMERAL:
        return None
    if startDepth == 4:
        return root
    for i in (LEFT, RIGHT):
        res = findPairToExplode(root[i], startDepth + 1)
        if res is not None:
            return res

def goDown(root, direction, threshold):
    if root[TYPE] == TYPE_NUMERAL:
        if root[VALUE] >= threshold:
            return root
        else:
            return None
    r = (LEFT, RIGHT) if direction == DIRECTION_RIGHT else (RIGHT, LEFT)
    for i in r:
        res = goDown(root[i], direction, threshold)
        if res is not None:
            return res
    return None


def goUp(root, direction):
    pId = root[PARENT]
    if pId is None:
        return None
    parent = globalTree[pId]
    if parent[RIGHT if direction == DIRECTION_RIGHT else LEFT] != root:
        res = goDown(parent[RIGHT if direction == DIRECTION_RIGHT else LEFT], direction, 0)
        if res is not None:
            return res
    return goUp(parent, direction)


def explode(root, numLeft, numRight):
    if numLeft is not None:
        numLeft[VALUE] += root[LEFT][VALUE]
    if numRight is not None:
        numRight[VALUE] += root[RIGHT][VALUE]
    root[TYPE] = TYPE_NUMERAL
    root[LEFT] = None
    root[RIGHT] = None
    root[VALUE] = 0


def tryToExplode(s):
    exploded = findPairToExplode(s, 0)
    if exploded is None:
        return False
    numL = goUp(exploded, DIRECTION_LEFT)
    numR = goUp(exploded, DIRECTION_RIGHT)
    explode(exploded, numL, numR)
    return True


def split(num):
    num[TYPE] = TYPE_PAIR
    num[LEFT] = {ID: getNextId(), PARENT: num[ID], TYPE: TYPE_NUMERAL, LEFT: None, RIGHT: None, VALUE: int(num[VALUE]/2)}
    num[RIGHT] = {ID: getNextId(), PARENT: num[ID], TYPE: TYPE_NUMERAL, LEFT: None, RIGHT: None, VALUE: math.ceil(num[VALUE] / 2)}
    globalTree[num[LEFT][ID]] = num[LEFT]
    globalTree[num[RIGHT][ID]] = num[RIGHT]
    #print("SPLIT ", num[VALUE], " into ", num[LEFT][VALUE], " and ", num[RIGHT][VALUE])
    num[VALUE] = None


def tryToSplit(s):
    num = goDown(s, DIRECTION_RIGHT, 10)
    if num is None:
        return False
    split(num)
    return True


def reduce(s):
    while True:
        if tryToExplode(s):
            continue
        if tryToSplit(s):
            continue
        break
    return s


def addPairs(p1, p2):
    res = {ID:getNextId(), PARENT: None, TYPE: TYPE_PAIR, LEFT: p1, RIGHT: p2, VALUE: None}
    globalTree[res[ID]] = res
    p1[PARENT] = res[ID]
    p2[PARENT] = res[ID]
    return res


def sumAllPairs(pairs):
    sumPairs = pairs[0]
    for p in pairs[1:]:
        #print(nodeToStr(sumPairs))
        #print("+ ", nodeToStr(p))
        sumPairs = addPairs(sumPairs, p)
        #print("= ", nodeToStr(sumPairs))
        reduce(sumPairs)
        #print("Reduced: ", nodeToStr(sumPairs))
        #print("===========")
    return sumPairs


def findMaxMagnitudeSum(strings):
    maxMag = None
    for a in range(len(strings)):
        print("A= ", a)
        for b in range(len(strings)):
            if a != b:
                pairs = []
                nextId = 0
                globalTree.clear()
                for d in strings:
                    pairs.append(parseNum(d))
                #print(nodeToStr(pairs[a]))
                #print("+ ", nodeToStr(pairs[b]))
                sumPair = addPairs(pairs[a], pairs[b])
                sumPair = reduce(sumPair)
                #print("= ", nodeToStr(sumPair))
                mag = magnitude(sumPair)
                #print("Magnitude: ", mag)
                if maxMag is None or mag > maxMag:
                    maxMag = mag
    return maxMag


def magnitude(node):
    if node[TYPE] == TYPE_NUMERAL:
        return node[VALUE]
    return 3 * magnitude(node[LEFT]) + 2 * magnitude(node[RIGHT])

def main():
    #data = "[[[[[9,8],1],2],3],4]"
    #data = "[7,[6,[5,[4,[3,2]]]]]"
    #data = "[[6,[5,[4,[3,2]]]],1]"
    #data = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
    #data = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    #d1 = "[[[[4,3],4],4],[7,[[8,4],9]]]"
    #d2 = "[1,1]"
    data = open("resources/day18_input.txt").read().splitlines()
    #pairs = []
    #for d in data:
     #   pairs.append(parseNum(d))
#    result = sumAllPairs(pairs)
#    print(nodeToStr(result))
#    print(magnitude(result))
    maxMag = findMaxMagnitudeSum(data)
    print(maxMag)


if __name__ == "__main__":
    main()

