# AoC: Day 3

houses = dict()

with open("input") as f:
    content = f.readlines()

pos         = (0, 0)
houses[pos] = 1


for c in content[0]:

    (x, y) = pos

    if c == '^':
        pos = (x, y + 1)

    elif c == 'v':
        pos = (x, y - 1)

    elif c == '<':
        pos = (x - 1, y)

    elif c == '>':
        pos = (x + 1, y)

    if pos in houses.keys():
        val = houses[pos]
        houses[pos] = val + 1
    else:
        houses[pos] = 1


total = 0

for key in houses.keys():
    if houses[key] >= 1:
        total += 1

print total
