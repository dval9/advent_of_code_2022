
def drop_sand():
    while True:
        sand = start

        for i in range(abyss + 1):
            if i == abyss:
                return

            if (sand[0], sand[1]+1) not in rocks:
                sand = (sand[0], sand[1]+1)
            elif (sand[0]-1, sand[1]+1) not in rocks:
                sand = (sand[0]-1, sand[1]+1)
            elif (sand[0]+1, sand[1]+1) not in rocks:
                sand = (sand[0]+1, sand[1]+1)
            else:
                rocks.add(sand)
                break


def drop_sand_again():
    while True:
        sand = start      

        for i in range(abyss + 100):            
            if (sand[0], sand[1]+1) not in rocks:
                sand = (sand[0], sand[1]+1)
            elif (sand[0]-1, sand[1]+1) not in rocks:
                sand = (sand[0]-1, sand[1]+1)
            elif (sand[0]+1, sand[1]+1) not in rocks:
                sand = (sand[0]+1, sand[1]+1)
            else:
                if sand == start:
                    return
                
                rocks.add(sand)
                break


file = open(r"./input14")
i = 0

start = (500, 0)
rocks = set()
rock_count = 0

for line in file:
    s = line.rstrip()
    s = s.split(' -> ')

    for i in range(len(s) - 1):
        a = s[i].split(',')
        b = s[i+1].split(',')

        for j in range(abs(int(a[0])-int(b[0])) + 1):
            if int(a[0]) < int(b[0]):
                rock = (int(a[0]) + j, int(a[1]))
            else:
                rock = (int(a[0]) - j, int(a[1]))
            rocks.add(rock)

        for j in range(abs(int(a[1])-int(b[1])) + 1):
            if int(a[1]) < int(b[1]):
                rock = (int(a[0]), int(a[1]) + j)
            else:
                rock = (int(a[0]), int(a[1]) - j)
            rocks.add(rock)

rocks2 = rocks.copy()

rock_count = len(rocks)
abyss = max(rocks, key=lambda y: y[1])[1] + 1

drop_sand()
print(len(rocks) - rock_count)

rocks = rocks2.copy()
min_x = min(rocks, key=lambda x: x[0])[0] - abyss
max_x = max(rocks, key=lambda x: x[0])[0] + abyss
floor = abyss + 1
for x in range(min_x, max_x+1, 1):
    rocks.add((x,floor))
rock_count = len(rocks)

drop_sand_again()
print(len(rocks) - rock_count + 1)

file.close()
