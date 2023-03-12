
import z3


def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def z3_abs(x):
    return z3.If(x >= 0, x, -x)


file = open(r"./input15")

sensors = set()
beacons = set()
seen = set()
# row = 10
# width = 20
row = 2000000
width = 4000000

for line in file:
    s = line.rstrip()
    s = s.split('=')

    s_x = int(s[1].split(',')[0])
    s_y = int(s[2].split(':')[0])
    b_x = int(s[3].split(',')[0])
    b_y = int(s[4])
    sensors.add(((s_x, s_y), (b_x, b_y)))
    beacons.add((b_x, b_y))

for sensor in sensors:
    s = sensor[0]
    b = sensor[1]
    r = manhattan(s, b)
    d = abs(s[1] - row)

    if d <= r:
        for i in range(s[0]-(r-d), s[0]+(r-d)+1, 1):
            seen.add((i, row))

i = seen - beacons
print(len(i))
file.close()

s = z3.Solver()
x, y = z3.Int('x'), z3.Int('y')
s.add(0 <= x)
s.add(0 <= y)
s.add(x <= width)
s.add(y <= width)

for a, b in sensors:
    m = manhattan(a, b)
    s.add(z3_abs(a[0] - x) + z3_abs(a[1] - y) > m)

assert s.check() == z3.sat
model = s.model()

print(model[x].as_long() * 4000000 + model[y].as_long())
