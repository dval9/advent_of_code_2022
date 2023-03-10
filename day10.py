

file = open(r"./input10")
i = 0


def update_signals():
    global cycle
    pixel = cycle % 40

    if pixel == 0:
        print('', end='\n')

    if pixel == x or abs(pixel - x) == 1:
        print('#', end='')
    else:
        print('.', end='')

    cycle += 1
    if (cycle % 20) == 0:
        signals.append(cycle * x)

    return cycle


cycle = 0
x = 1
signals = []

for line in file:
    s = line.rstrip().split(' ')

    if s[0] == 'noop':
        update_signals()
    else:
        update_signals()
        update_signals()
        x += int(s[1])

i = signals[0] + signals[2] + signals[4] + \
    signals[6] + signals[8] + signals[10]

print('', end='\n')
print(i)
file.close()
