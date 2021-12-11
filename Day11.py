def incCheckAndFlash(x, y, octopuses, flashes):
    octopuses[(x, y)] += 1
    if (x, y) in flashes:
        return
    if octopuses[(x, y)] > 9:
        flashes.add((x, y))
        for nx in range(0 if x == 0 else x-1, 10 if x == 9 else x+2):
            for ny in range(0 if y == 0 else y-1, 10 if y == 9 else y+2):
                if nx == x and ny == y:
                    continue
                incCheckAndFlash(nx, ny, octopuses, flashes)

def main():
    dataLines = open("resources/day11_input.txt").read().splitlines()
    octopuses = {}
    y = 0
    for s in dataLines:
        x = 0
        for c in s:
            octopuses[(x, y)] = int(c)
            x += 1
        y += 1
    numFlashes = 0
    step = 0
    stop = False
    #for step in range(100):
    while not stop:
        step += 1
        flashes = set()
        for (x, y) in octopuses:
            incCheckAndFlash(x, y, octopuses, flashes)
        numFlashes += len(flashes)
        if len(flashes) == len(octopuses):
            stop = True
        #print("Step ", step, ", flashes ", len(flashes))
        while len(flashes) > 0:
            octopuses[flashes.pop()] = 0
    print("Total flashes: ", numFlashes)
    print("Step where all flashed: ", step)

if __name__ == '__main__':
    main()