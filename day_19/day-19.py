# AoC: Day 19

with open("input") as f:
    lines = f.readlines()


replace = []
target  = lines[-1].strip()
output  = set()

for line in lines:
    if "=>" in line:
        (a, b) = line.split("=>")
        a      = a.split()[0]
        b      = b.split()[0]
        replace.append((b, a))


def substitute(string, pos, s, t):
    return string[:pos] + t + string[pos + len(s):]


def replaceAll(target, subst, pos, firstRun):

    (s, t)  = subst

    if firstRun:
        pos = target.find(s, 0)

    if pos == -1:
        return

    res     = substitute(target, pos, s, t)

    output.append(res)

    nextPos = tmp.find(s, pos + 1)

    return replaceAll(target, subst, nextPos, False)


i          = 0
tmp        = target
candidates = [tmp]


while True:

    newCandidates = []

    # for each candidate string:
    for elem in candidates:

        if "e" in elem:
            # illegal reduction
            continue

        # take current string, attempt to perform all replacements
        for (s, t) in replace:
            if s in elem:
                output = []  #set()
                replaceAll( elem, (s, t), 0, True)
                newCandidates += output

    i += 1

    if "e" in newCandidates:
        break

    # a bit hackish, but without sorting intermediate results,
    # the correct solution (200) is reached reasonably quickly
    
    #candidates = newCandidates[:5000]
    #candidates = newCandidates[:2500]
    #candidates = newCandidates[:1250]
    #candidates = newCandidates[:125]
    #candidates = newCandidates[:50]
    #candidates = newCandidates[:25]
    #candidates = newCandidates[:5]

    # interestingly, just using the first result is enough:
    candidates = newCandidates[:1]

    print(i)


print("Number of steps: ", i)