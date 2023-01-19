pack = [int(x) for x in input().split()]
pack.sort()
if 0 in pack:
    for i in pack:
        if (pack[i] != 0):
            pack[0], pack[i] = pack[i], pack[0]
            break
for x in pack:
    print(x, end="")
