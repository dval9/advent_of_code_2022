
def update_tail(h_x, h_y, t_x, t_y):
    if abs(h_x - t_x) == 2:
        if h_y - t_y == 1:
            if h_x > t_x:
                t_x += 1
                t_y += 1
            else:
                t_x -= 1
                t_y += 1
        elif h_y - t_y == -1:
            if h_x > t_x:
                t_x += 1
                t_y -= 1
            else:
                t_x -= 1
                t_y -= 1
        else:
            if h_x > t_x:
                t_x += 1
            else:
                t_x -= 1
    elif abs(h_y - t_y) == 2:
        if h_x - t_x == 1:
            if h_y > t_y:
                t_y += 1
                t_x += 1
            else:
                t_y -= 1
                t_x += 1
        elif h_x - t_x == -1:
            if h_y > t_y:
                t_y += 1
                t_x -= 1
            else:
                t_y -= 1
                t_x -= 1
        else:
            if h_y > t_y:
                t_y += 1
            else:
                t_y -= 1

    return t_x, t_y


file = open(r"./input9")
i = 0
pos = [[0 for x in range(500)] for y in range(500)]
h_x, t_x = 250, 250
h_y, t_y = 250, 250
pos[t_y][t_x] = 1

for line in file:
    s = line.rstrip().split(' ')
    if s[0] == 'R':
        for i in range(int(s[1])):
            h_x += 1
            t_x, t_y = update_tail(h_x, h_y, t_x, t_y)
            pos[t_y][t_x] = 1
    if s[0] == 'L':
        for i in range(int(s[1])):
            h_x -= 1
            t_x, t_y = update_tail(h_x, h_y, t_x, t_y)
            pos[t_y][t_x] = 1
    if s[0] == 'D':
        for i in range(int(s[1])):
            h_y += 1
            t_x, t_y = update_tail(h_x, h_y, t_x, t_y)
            pos[t_y][t_x] = 1
    if s[0] == 'U':
        for i in range(int(s[1])):
            h_y -= 1
            t_x, t_y = update_tail(h_x, h_y, t_x, t_y)
            pos[t_y][t_x] = 1

i = sum(map(sum, pos))

print(i)
file.close()


def update_pos():
    pos[knots[num_knots - 1][0]][knots[num_knots - 1][1]] = 1


file = open(r"./input9")
i = 0
pos = [[0 for x in range(500)] for y in range(500)]
num_knots = 10
knots = [[250, 250] for x in range(num_knots)]
update_pos()

for line in file:
    s = line.rstrip().split(' ')

    if s[0] == 'R':
        for i in range(int(s[1])):
            knots[0][0] += 1
            for i in range(len(knots) - 1):
                knots[i+1][0], knots[i+1][1] = update_tail(
                    knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1])
            update_pos()
    if s[0] == 'L':
        for i in range(int(s[1])):
            knots[0][0] -= 1
            for i in range(len(knots) - 1):
                knots[i+1][0], knots[i+1][1] = update_tail(
                    knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1])
            update_pos()
    if s[0] == 'D':
        for i in range(int(s[1])):
            knots[0][1] += 1
            for i in range(len(knots) - 1):
                knots[i+1][0], knots[i+1][1] = update_tail(
                    knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1])
            update_pos()
    if s[0] == 'U':
        for i in range(int(s[1])):
            knots[0][1] -= 1
            for i in range(len(knots) - 1):
                knots[i+1][0], knots[i+1][1] = update_tail(
                    knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1])
            update_pos()

i = sum(map(sum, pos))

print(i)
file.close()


file = open(r"./input9")
# stole this
rope = [0] * 10
seen = [set([x]) for x in rope]
dirs = {'L': +1, 'R': -1, 'D': 1j, 'U': -1j}


def sign(x): return complex((x.real > 0) -
                            (x.real < 0), (x.imag > 0) - (x.imag < 0))


for line in file:
    for _ in range(int(line[2:])):
        rope[0] += dirs[line[0]]

        for i in range(1, 10):
            dist = rope[i-1] - rope[i]
            if abs(dist) >= 2:
                rope[i] += sign(dist)
                seen[i].add(rope[i])

print(len(seen[1]), len(seen[9]))

file.close()
