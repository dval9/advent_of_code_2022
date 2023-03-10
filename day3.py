

file = open(r"./input3")
priority_sum = 0


def calculate_prio(a, b):
    priority = 0
    for c in a:
        for d in b:
            if c == d:
                if str.islower(c):
                    priority = ord(c)-96
                else:
                    priority = ord(c)-38
                return priority
    return priority


def find_badge(a, b, c):
    priority = 0
    for d in a:
        for e in b:
            if d == e:
                for f in c:
                    if d == f:
                        if str.islower(d):
                            priority = ord(d)-96
                        else:
                            priority = ord(d)-38
                        return priority
    return priority


for line in file:
    backpack = line.rstrip()

    a = backpack[:len(backpack)//2]
    b = backpack[len(backpack)//2:]

    priority_sum += calculate_prio(a, b)

print(priority_sum)
file.close()


file = open(r"./input3")
priority_sum = 0
bag_count = 0
bags = []

for line in file:
    backpack = line.rstrip()

    bags.append(backpack)
    bag_count += 1

    if bag_count == 3:
        priority_sum += find_badge(bags[0], bags[1], bags[2])
        bag_count = 0
        bags = []

print(priority_sum)
file.close()
