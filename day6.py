

file = open(r"./input6")
i = 4

for line in file:    
    s = list(line.rstrip())

    while len(s) > 4:

        sop = s[:4]
        if len(sop) == len(set(sop)):
            break
        s.pop(0)
        i += 1

print(i)
file.close()


file = open(r"./input6")
i = 14

for line in file:    
    s = list(line.rstrip())

    while len(s) > 14:

        sop = s[:14]
        if len(sop) == len(set(sop)):
            break
        s.pop(0)
        i += 1

print(i)
file.close()