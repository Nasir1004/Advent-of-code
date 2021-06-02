# AoC: Day 20

target = 29000000
limit  = 1000000
arr    = [ 0 for i in range(limit + 1)]

i = 1
while True:

    if i > limit:
        break

    j         = i
    delivered = 0

    while j < limit + 1:

        if delivered >= 50:
            break

        arr[j]    += i * 11
        j         += i
        delivered += 1

    i += 1


for idx in range(len(arr)):
    if arr[idx] >= target:
        print idx
        break
