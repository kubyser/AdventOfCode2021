import math


def simulate(xs, ys, minx, maxx, miny, maxy):
    x = 0
    y = 0
    stop = False
    maxheight = y
    while not stop:
        x += xs
        y += ys
        if xs > 0:
            xs -= 1
        ys -= 1
        if y > maxheight:
            maxheight = y
        if (minx <= x <= maxx) and (miny <= y <= maxy):
            return maxheight
        if x > maxx or y < miny:
            stop = True
    return None


def main():
    #data = "target area: x=20..30, y=-10..-5"
    data = open("resources/day17_input.txt").read().splitlines()[0]
    data = data.split(" ")
    minx = int(data[2][2:-1].split("..")[0])
    maxx = int(data[2][2:-1].split("..")[1])
    miny = int(data[3][2:].split("..")[0])
    maxy = int(data[3][2:].split("..")[1])
    minxs = int((math.sqrt(1 + 8 * minx) - 1) / 2) + 1
    maxxs = maxx
    minys = miny
    maxys = -miny
    maxheight = None
    numresults = 0
    for xs in range(minxs, maxxs+1):
        for ys in range(minys, maxys+1):
            res = simulate(xs, ys, minx, maxx, miny, maxy)
            if res is not None:
                numresults += 1
                print(numresults, ": ", xs, ys)
                if maxheight is None or res > maxheight:
                    maxheight = res
                    print("New max height: ", maxheight)
    print("Total results: ", numresults, "Max height: ", maxheight)

if __name__ == "__main__":
    main()