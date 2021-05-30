# AoC: Day 17

import itertools

SIZE  = 150


with open("input") as f:
    lines = f.readlines()

elems = list(map(lambda x: int(x), lines))
count = dict()

for i in range(0, len(elems) + 1):
    for subset in itertools.combinations(elems, i):
        subset = list(subset)
        if sum(subset) == SIZE:

            length = len(subset)
            if length not in count.keys():
                count[length] = 1
            else:
                count[length] += 1

print (count[min(count.keys())])