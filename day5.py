

stacks = [['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
          ['N', 'V', 'G', 'P', 'H', 'W', 'B'],
          ['F', 'W', 'B', 'J', 'G'],
          ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
          ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
          ['B', 'C', 'W', 'G', 'F', 'S'],
          ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
          ['F', 'S', 'W', 'T'],
          ['N', 'C', 'R']]

file = open(r"./input5")

for line in file:
    moves = line.rstrip()

    moves = moves.split(' ')
    c = int(moves[1])
    f = int(moves[3])
    t = int(moves[5])

    i = 0
    while i < c:
        stacks[t-1].append(stacks[f-1].pop())
        i += 1

order = ''
for stack in stacks:
    order += stack.pop()
print(order)
file.close()

stacks = [['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
          ['N', 'V', 'G', 'P', 'H', 'W', 'B'],
          ['F', 'W', 'B', 'J', 'G'],
          ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
          ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
          ['B', 'C', 'W', 'G', 'F', 'S'],
          ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
          ['F', 'S', 'W', 'T'],
          ['N', 'C', 'R']]

file = open(r"./input5")

for line in file:
    moves = line.rstrip()

    moves = moves.split(' ')
    c = int(moves[1])
    f = int(moves[3])
    t = int(moves[5])

    i = 0
    temp = []
    while i < c:
        temp.append(stacks[f-1].pop())
        i += 1

    i = 0
    while i < c:
        stacks[t-1].append(temp.pop())
        i += 1

order = ''
for stack in stacks:
    order += stack.pop()
print(order)
file.close()
