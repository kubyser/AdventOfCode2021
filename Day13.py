def printDots(dots):
    maxX = max(x for (x, y) in dots)
    maxY = max(y for (x, y) in dots)
    for y in range(maxY + 1):
        s = ""
        for x in range(maxX + 1):
            s += "#" if (x, y) in dots else " "
        print(s)


def main():
    data = open("resources/day13_input.txt").read().splitlines()
    dots = set()
    n = 0
    for d in data:
        if d == "":
            break
        xy = d.split(",")
        dots.add((int(xy[0]), int(xy[1])))
        n += 1
    instructions = data[n+1:]
    for s in instructions:
        s = s.split()[2]
        pos = int(s.split("=")[1])
        if s[0] == "y":
            down = [(x, y) for (x, y) in dots if y > pos]
            for (x, y) in down:
                dots.add((x, 2 * pos - y))
                dots.remove((x, y))
        else:
            right = [(x, y) for (x, y) in dots if x > pos]
            for (x, y) in right:
                dots.add((2 * pos - x, y))
                dots.remove((x, y))
#        break
    print(len(dots))
    printDots(dots)


if __name__ == '__main__':
    main()