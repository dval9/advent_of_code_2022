

file = open(r"./input1")
elf = 1
elves = {}
total_cals = 0

for line in file:
    cals = line.rstrip()

    if cals == "":
        elves[elf] = total_cals
        total_cals = 0
        elf += 1
    else:
        total_cals += int(cals)

print(max(elves, key=elves.get))
print(max(elves.values()))

sorted = sorted(elves, key=elves.get, reverse=True)
print(elves[sorted[0]] + elves[sorted[1]] + elves[sorted[2]])

file.close()
