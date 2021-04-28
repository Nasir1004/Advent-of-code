# AoC: Day 7

signals = dict()


with open("input") as f:
    instructions = f.readlines()


for i in instructions:

    tmp = i.split("->")

    val = tmp[0]
    val = val.split()
    var = tmp[1].strip()

    # signal
    if len(val) == 1 and val[0].isdigit():
        val          = int(val[0])
        signals[var] = val

    elif len(val) == 1 and not val[0].isdigit():
        signals[var] = ("SUBST", val[0])

    elif "AND" in val or "OR" in val or "LSHIFT" in val or "RSHIFT" in val:
        (a, op, b)   = val[0], val[1], val[2]
        signals[var] = (op, a, b)

    # NOT
    elif "NOT" in val:
        (op, a) = val[0], val[1]
        signals[var] = (op, a)


signals['b'] = 956


# substitute
while True:

    for key in signals.keys():

        val = signals[key]

        if str(val).isdigit():
            continue

        op = val[0]

        if op == "NOT":
            (_, var) = val
            tmp      = signals[var]

            if str(tmp).isdigit():
                signals[key] = ~tmp & 65535

        elif op == "AND":
            (_, a, b) = val

            if not str(a).isdigit():
                a = signals[a]

            if not str(b).isdigit():
                b = signals[b]

            if str(a).isdigit() and str(b).isdigit():
                signals[key] = int(a) & b

        elif op == "OR":
            (_, a, b) = val
            a = signals[a]
            b = signals[b]

            if str(a).isdigit() and str(b).isdigit():
                signals[key] = a | b

        elif op == "LSHIFT":
            (_, a, n) = val
            a = signals[a]

            if str(a).isdigit():
                signals[key] = a << int(n)

        elif op == "RSHIFT":
            (_, a, n) = val
            a = signals[a]

            if str(a).isdigit():
                signals[key] = a >> int(n)

        elif op == "SUBST":
            (_, a) = val

            a = signals[a]

            if str(a).isdigit():
                signals[key] = a

    done = True
    for key in signals.keys():
         tmp = signals[key]

         if not str(tmp).isdigit():
             done = False
             break

    if done:
        print(signals)
        print(signals['a'])
        break
