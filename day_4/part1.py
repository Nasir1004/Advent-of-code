# AoC: Day 4

import hashlib

key = "iwrupvqb"
i   = 0

while True:
    tmp    = key + str(i)
    answer = hashlib.md5(tmp).hexdigest()

    if answer.startswith("00000"):
        print i, answer
        break

    i += 1