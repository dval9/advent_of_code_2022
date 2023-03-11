
import collections


def bfs(grid, start, goal):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (ord(grid[y2][x2]) - ord(grid[y][x])) <= 1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


def in_list(c, classes):
    for i, sublist in enumerate(classes):
        if c in sublist:
            return i
    return -1


file = open(r"./input12")
i = 0

start, goal = 'S', 'E'
grid = []

for line in file:
    grid.append(line.rstrip())

width, height = len(grid[0]), len(grid)
start = [in_list(start, grid), in_list(start, grid[in_list(start, grid)])]
goal = [in_list(goal, grid), in_list(goal, grid[in_list(goal, grid)])]
grid[start[0]] = grid[start[0]].replace('S', 'a')
grid[goal[0]] = grid[goal[0]].replace('E', 'z')

path = bfs(grid, (start[1], start[0]), (goal[1], goal[0]))
i = len(path) - 1
print(i)

starts = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'a':
            starts.append((j, i))

best_length = 999
for s in starts:
    path = bfs(grid, s, (goal[1], goal[0]))
    if path is not None and len(path) < best_length:
        best_length = len(path)

i = best_length - 1
print(i)
file.close()
