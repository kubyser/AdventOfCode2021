def printVents(vents):
    maxx = max(v[0] for v in vents)
    maxy = max(v[1] for v in vents)
    for y in range(maxy+1):
        s = ""
        for x in range(maxx+1):
            s += str(vents[x, y]) if (x, y) in vents else "."
        print(s)

def findDangerousVents(data, includeDiagonals):
    vents = {}
    for s in data:
        s1 = s.split(" -> ")
        x1 = int(s1[0].split(",")[0])
        y1 = int(s1[0].split(",")[1])
        x2 = int(s1[1].split(",")[0])
        y2 = int(s1[1].split(",")[1])
        if x1 == x2 or y1 == y2 or includeDiagonals:
            xinc = 1 if x1 < x2 else -1 if x1 > x2 else 0
            yinc = 1 if y1 < y2 else -1 if y1 > y2 else 0
            xpos = x1
            ypos = y1
            stop = False
            while not stop:
                if (xpos, ypos) in vents:
                    vents[(xpos, ypos)] += 1
                else:
                    vents[(xpos, ypos)] = 1
                stop = xpos == x2 and ypos == y2
                xpos += xinc
                ypos += yinc
#    printVents(vents)
    res = sum(map(lambda x: vents[x] > 1, vents))
    return res


def main():
    data = open("resources/day5_input.txt", "r").read().splitlines()
    res = findDangerousVents(data, False)
    print("Result part 1: ", res)
    res = findDangerousVents(data, True)
    print("Result part 2: ", res)

if __name__ == "__main__":
    main()