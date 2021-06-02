# AoC: Day 18

with open("input") as f:
    lines = f.readlines()


def processLine(line):

    res = []

    line = line.strip()

    for i in range(len(line)):
        if line[i] == "#":
            res.append(1)
        elif line[i] == ".":
            res.append(0)

    return res


m = map(lambda x: processLine(x), lines)
w = len(m)

def validPos(mat, pos):

    n      = len(mat)
    (x, y) = pos

    c1 = x >= 0 and y >= 0
    c2 = x <  n and y <  n

    return c1 and c2


def neighborsOn(mat, pos):

    (x, y)      = pos

    p1          = (x + 1, y    )
    p2          = (x - 1, y    )
    p3          = (x,     y + 1)
    p4          = (x,     y - 1)
    p5          = (x + 1, y + 1)
    p6          = (x - 1, y - 1)
    p7          = (x + 1, y - 1)
    p8          = (x - 1, y + 1)

    allPos      = [p1, p2, p3, p4, p5, p6, p7, p8]
    relevantPos = filter(lambda x: validPos(mat, x), allPos)
    isOn        = list(map(lambda (x, y): mat[x][y], relevantPos ))

    return sum(isOn)


def getNewVal(on, val, pos, corners):
    """
    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    """

    (x, y) = pos

    # corner lights are always on
    if (x, y) in corners:
        return 1

    if val == 0:
        if on == 3:
            return 1

    elif val == 1:
        if not (on == 2 or on == 3):
            return 0

    return val


def updateMatrix(mat):

    l         = len(mat)
    newMatrix = []
    corners   = [(0, 0), (0, l-1), (l-1, 0), (l-1, l-1)]

    for i in range(l):
        row = []

        for j in range(l):
            val  = mat[i][j]
            on   = neighborsOn(mat, (i, j))
            row.append(getNewVal(on, val, (i, j), corners))

        newMatrix.append(row)

    return newMatrix


def printMat(mat):
    for row in mat:
        print(row)


for i in range(100):
    print(i)
    m = updateMatrix(m)


print (sum( map(lambda x: sum(x), m) ))