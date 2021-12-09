def printbasin(basins, maxx, maxy):
    print("Basins: ")
    for basin in basins:
        print("Basin ", basin, " size ", len(basins[basin]))
        print(basins[basin])
        for y in range(maxy):
                s = ""
                for x in range(maxx):
                    s += "#" if (x, y) in basins[basin] else "."
                print(s)

def main():
    datalines = open("resources/day9_input.txt", "r").read().splitlines()
    data = [[0] * len(datalines) for d in datalines[0]]
    line = 0
    for d in datalines:
        pos = 0
        for c in d:
            data[pos][line] = int(c)
            pos += 1
        line += 1
    basins = {}
    maptobasin = {}
    numbasins = 0
    for y in range(len(data[0])):
        for x in range(len(data)):
            a = data[x][y]
            if a != 9:
                if x > 0 and (x-1, y) in maptobasin:
                    maptobasin[(x, y)] = maptobasin[(x-1, y)]
                    basins[maptobasin[(x, y)]].append((x, y))
                if y > 0 and (x, y-1) in maptobasin:
                    if (x, y) in maptobasin and maptobasin[(x, y)] != maptobasin[(x, y-1)]:
                        oldbasin = maptobasin[(x, y)]
                        newbasin = maptobasin[(x, y-1)]
                        for b in basins[oldbasin]:
                            maptobasin[b] = newbasin
                        basins[newbasin] += basins[oldbasin]
                        basins.pop(oldbasin)
                    elif (x, y) not in maptobasin:
                        maptobasin[(x, y)] = maptobasin[(x, y-1)]
                        basins[maptobasin[(x, y)]].append((x, y))
                if (x, y) not in maptobasin:
                    maptobasin[(x, y)] = numbasins
                    basins[numbasins] = [(x, y)]
                    numbasins += 1
    #printbasin(basins, len(data), len(data[0]))
    sizes = [len(basins[b]) for b in basins]
    sizes.sort(reverse=True)
    print(sizes)
    res = sizes[0] * sizes[1] * sizes[2]
    print("Product: ", res)




if __name__ == "__main__":
    main()