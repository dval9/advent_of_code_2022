

file = open(r"./input7")
i = 0

path = ['/']
dirs = {'/'.join(str(x) for x in path): 0}

for line in file:
    s = line.rstrip().split(' ')
    
    if s[0] == '$':
        if s[1] == 'ls':
            pass
        elif s[1] == 'cd':
            if s[2] == '..':
                path.pop()
            elif s[2] == '/':
                path = ['/']
            else:
                path.append(s[2])
                dirs['/'.join(str(x) for x in path)] = 0
    else:
        if s[0] != 'dir':
            temp = path.copy()
            while len(temp) > 0:
                dirs['/'.join(str(x) for x in temp)] += int(s[0])
                temp.pop()

for k, v in dirs.items():
    if v < 100000:
        i += v;

print(i)
file.close()

space_target = dirs['/']  - (70000000 - 30000000)
sorted = sorted(dirs, key=dirs.get)

i = 0
while dirs[sorted[i]] < space_target:
    i += 1
print(dirs[sorted[i]])