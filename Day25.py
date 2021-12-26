EAST = 0
SOUTH = 1

width = None
height = None

def printField(cucumbers):
    global width
    global height
    for y in range(height):
        s = ""
        for x in range(width):
            if (x, y) in cucumbers[EAST]:
                s += ">"
            elif (x, y) in cucumbers[SOUTH]:
                s += "v"
            else:
                s += "."
        print(s)
    print("=============")


def getDestination(direction, x, y):
    global width
    global height
    if direction == EAST:
        x += 1
        if x >= width:
            x = 0
    else:
        y += 1
        if y >= height:
            y = 0
    return x, y


def tryMove(cucumbers, field):
    tomove = {EAST: set(), SOUTH: set()}
    for direction in (EAST, SOUTH):
        for x, y in cucumbers[direction]:
            x1, y1 = getDestination(direction, x, y)
            if not field[x1][y1]:
                tomove[direction].add((x, y, x1, y1))
        for x, y, x1, y1 in tomove[direction]:
            cucumbers[direction].remove((x, y))
            cucumbers[direction].add((x1, y1))
            field[x][y] = False
            field[x1][y1] = True
    return len(tomove[EAST]) > 0 or len(tomove[SOUTH]) > 0


def main():
    data = open("resources/day25_input.txt").read().splitlines()
    global width
    global height
    width = len(data[0])
    height = len(data)
    field = [[False] * height for i in range(width)]
    cucumbers = {EAST: set(), SOUTH: set()}
    for i in range(width):
        for j in range(height):
            c = data[j][i]
            if c in (">", "v"):
                field[i][j] = True
                cucumbers[EAST if c == '>' else SOUTH].add((i, j))
    printField(cucumbers)
    steps = 1
    while tryMove(cucumbers, field):
        steps += 1
    print("Stopped after ", steps, " steps")



if __name__ == "__main__":
    main()

