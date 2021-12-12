import copy

SMALLVISITED = 0
DOUBLEVISITED = 1
PATH = 2
cavesMap = {}
largeCaves = set()
foundRoutes = []

part2 = True

def findRoutesFrom(node, route):
    newRoute = copy.deepcopy(route)
    if node not in largeCaves:
        if node in newRoute[SMALLVISITED]:
            newRoute[DOUBLEVISITED] = node
        else:
            newRoute[SMALLVISITED].add(node)
    newRoute[PATH].append(node)
    if node == 'end':
        foundRoutes.append(newRoute)
        return
    for dest in cavesMap[node]:
        if dest in largeCaves or dest not in newRoute[SMALLVISITED] or (part2 and dest != 'start' and newRoute[DOUBLEVISITED] == None):
            findRoutesFrom(dest, newRoute)

def main():
    lines = open("resources/day12_input.txt").read().splitlines()
    for s in lines:
        ss = s.split("-")
        for sn in ss:
            if sn.isupper() and sn not in largeCaves:
                largeCaves.add(sn)
        if ss[0] in cavesMap:
            cavesMap[ss[0]].append(ss[1])
        else:
            cavesMap[ss[0]] = [ss[1]]
        if ss[1] in cavesMap:
            cavesMap[ss[1]].append(ss[0])
        else:
            cavesMap[ss[1]] = [ss[0]]
    #print(largeCaves)
    #print(cavesMap)
    startRoute = {SMALLVISITED: set(), DOUBLEVISITED: None, PATH: []}
    findRoutesFrom("start", startRoute)
    print("Routes found: ", len(foundRoutes))
    #for r in foundRoutes:
    #    print(r)


if __name__ == '__main__':
    main()
