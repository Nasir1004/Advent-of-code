# AoC: Day 5
import string

def p1(s):

    az = string.ascii_lowercase

    for x in az:
        for y in az:
            if s.count(x + y) >= 2:
                return True

    return False


def p2(s):

    pairs       = allPairs(s, [])
    letterPairs = []

    for c in string.ascii_lowercase:
        letterPairs.append(c + c)

    for el in letterPairs:
        if el in pairs:
            return True

    return False


def allPairs(s, acc):

    if len(s) <= 2:
        return acc

    else:
        acc.append(s[0] + s[2])
        return allPairs(s[1:], acc)


total = 0

with open("input") as f:
    content = f.readlines()


for elem in content:
    if p1(elem) and p2(elem):
        total += 1

print total