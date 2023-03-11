
import ast
from functools import cmp_to_key


def in_list(c, classes):
    for i, sublist in enumerate(classes):
        if c == sublist:
            return i
    return -1


def packet_eval(p1, p2):

    i = 0
    while i < len(p1) and i < len(p2):
        if type(p1[i]) is int and type(p2[i]) is int:
            if p1[i] < p2[i]:
                return 1
            elif p1[i] > p2[i]:
                return -1
        elif type(p1[i]) is list and type(p2[i]) is list:
            result = packet_eval(p1[i], p2[i])
            if result is not None:
                return result
        elif type(p1[i]) is list and type(p2[i]) is int:
            result = packet_eval(p1[i], [p2[i]])
            if result is not None:
                return result
        elif type(p1[i]) is int and type(p2[i]) is list:
            result = packet_eval([p1[i]], p2[i])
            if result is not None:
                return result
        i += 1

    if i == len(p1) and i < len(p2):
        return 1
    elif i < len(p1) and i == len(p2):
        return -1


file = open(r"./input13")
lines = file.readlines()

index = 0
index_sum = 0
d1 = [[2]]
d2 = [[6]]
packets = [d1, d2]
for i in range(0, len(lines)-1, 3):
    p1 = ast.literal_eval(lines[i].rstrip())
    p2 = ast.literal_eval(lines[i+1].rstrip())
    index += 1
    packets.append(p1)
    packets.append(p2)

    # print(str(p1) + ' vs ' + str(p2))
    # print(packet_eval(p1, p2))

    result = packet_eval(p1, p2)
    if result == 1:
        index_sum += index


print(index_sum)
file.close()


packets.sort(key=cmp_to_key(packet_eval), reverse=True)
i1 = in_list(d1, packets) + 1
i2 = in_list(d2, packets) + 1

print(i1 * i2)
