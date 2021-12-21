def printImage(image):
    minx = None
    maxx = None
    miny = None
    maxy = None
    for (x, y) in image:
        if minx is None or x < minx:
            minx = x
        if miny is None or y < miny:
            miny = y
        if maxx is None or x > maxx:
            maxx = x
        if maxy is None or y > maxy:
            maxy = y
    print("Minx = ", minx, " Miny = ", miny)
    for y in range(miny, maxy+1):
        s = ""
        for x in range(minx, maxx+1):
            s += "#" if (x, y) in image else "."
        print(s)


def processDot(x, y, image, algo, processed, defState):
    s = ""
    for j in (y-1, y, y+1):
        for i in (x-1, x, x+1):
            if (i, j) in image:
                s += "1" if image[(i, j)] == 1 else "0"
            else:
                s += "1" if defState == 1 else "0"
    num = int(s, 2)
    processed[x, y] = 1 if algo[num] else 0


def run(image, algo, defState):
    processed = {}
    for (x, y) in image:
        for j in (y-1, y, y+1):
            for i in (x-1, x, x+1):
                if (i, j) not in processed:
                    processDot(i, j, image, algo, processed, defState)
    for (x, y) in processed:
        image[(x, y)] = processed[(x, y)]


def getLitCount(image):
    return(len(list(filter(lambda x: image[x] == 1, image))))


def main():
    data = open("resources/day20_input.txt").read().splitlines()
    algo = [False] * len(data[0])
    for i in range(len(data[0])):
        if data[0][i] == "#":
            algo[i] = True
    image = {}
    y = 0
    for s in data[2:]:
        x = 0
        for c in s:
            image[(x, y)] = 1 if c == "#" else 0
            x += 1
        y += 1
    print(getLitCount(image))
    defState = 0
    for i in range(50):
        run(image, algo, defState)
        defState = 0 if defState == 1 else 1
        print(getLitCount(image))


if __name__ == "__main__":
    main()

