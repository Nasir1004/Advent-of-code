def presence(xs):
	if xs == []:
		return 1
	else:
		return xs[0] * presence(xs[1:])

total = 0

with open("input") as f:
    content = f.readlines()

for c in content:
    dimention = list(map(lambda x: int(x), c.split('x')))
    dimention.sort()
    total += 2 * (dimention[0] + dimention[1]) + presence(dimention)

print(total)
# 1598415