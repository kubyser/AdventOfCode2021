def main():
    data = open("resources/day15_input.txt").read().splitlines()
    x = 0
    y = 0
    riskmap = {}
    for s in data:
        x = 0
        for c in s:
            riskmap[(x, y)] = int(c)
            x += 1
        y += 1
    width = x
    height = y
    # part2
    for x in range(width):
        for y in range(height):
            for r in range(1, 5):
                riskmap[(x + width*r, y)] = riskmap[(x, y)] + r if riskmap[(x, y)] + r <= 9 else riskmap[(x, y)] + r - 9
    width *= 5
    for x in range(width):
        for y in range(height):
            for r in range(1, 5):
                riskmap[(x, y + height*r)] = riskmap[(x, y)] + r if riskmap[(x, y)] + r <= 9 else riskmap[(x, y)] + r - 9
    height *= 5
    routemap = {}
    toexplore = {(0, 0): (0, [])}
    step = 0
    while len(toexplore) > 0:
        (x, y) = next(iter(toexplore.keys()))
        minrisk = toexplore[(x, y)][0]
        for (a, b) in toexplore:
            if toexplore[(a, b)][0] < minrisk:
                (x, y) = (a, b)
                minrisk = toexplore[(x, y)][0]
        (risk, route) = toexplore.pop((x, y))
        if (x, y) not in routemap or routemap[(x, y)][0] > risk:
            routemap[(x, y)] = (risk, route)
            for (nx, ny) in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if nx >= 0 and nx < width and ny >= 0 and ny < height:
                    newrisk = risk + riskmap[(nx, ny)]
                    if (nx, ny) not in routemap or routemap[(nx, ny)][0] > newrisk:
                        if (nx, ny) not in toexplore or toexplore[(nx, ny)][0] > newrisk:
                            toexplore[(nx, ny)] = (newrisk, route + [(nx, ny)])
        #print("ToExplore: ", toexplore)
        #print("RouteMap: ", routemap)
        step += 1
    print(routemap[(width-1, height-1)])

if __name__ == "__main__":
    main()

