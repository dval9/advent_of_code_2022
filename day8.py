

def visible(i, j, height, dir):
    vis = 1
    scenic = 0

    if dir == 'u':
        while j >= 0 and vis == 1:
            if map[j][i] >= height:
                vis = 0
            scenic += 1
            j -= 1
    elif dir == 'l':
        while i >= 0 and vis == 1:
            if map[j][i] >= height:
                vis = 0
            scenic += 1
            i -= 1
    elif dir == 'd':
        while j < len(map) and vis == 1:
            if map[j][i] >= height:
                vis = 0
            scenic += 1
            j += 1
    elif dir == 'r':
        while i < len(map) and vis == 1:
            if map[j][i] >= height:
                vis = 0
            scenic += 1
            i += 1

    return [vis, scenic]


file = open(r"./input8")
count = 0
map = []

for line in file:
    map.append([int(s) for s in line.rstrip()])

count += len(map) * 2 + (len(map[0]) - 2) * 2

i = 1
j = 1
best_score = 0
while i < (len(map[0]) - 1):
    while j < (len(map) - 1):
        height = map[j][i]

        vis = max(visible(i, j-1, height, 'u')[0],
                  visible(i-1, j, height, 'l')[0],
                  visible(i, j+1, height, 'd')[0],
                  visible(i+1, j, height, 'r')[0])
        count += vis

        score = visible(i, j-1, height, 'u')[1] * visible(i-1, j, height, 'l')[
            1] * visible(i, j+1, height, 'd')[1] * visible(i+1, j, height, 'r')[1]
        if score > best_score:
            best_score = score

        j += 1
    i += 1
    j = 1

print(count)
print(best_score)
file.close()
