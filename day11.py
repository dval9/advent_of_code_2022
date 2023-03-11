

# file = open(r"./input3")
i = 0

# for line in file:
#    s = line.rstrip()


class Monkey:
    def __init__(self, items, op, test, true_act, false_act):
        self.inspections = 0
        self.items = items
        self.op = op
        self.test = test
        self.true_act = true_act
        self.false_act = false_act

    def inspect(self):
        if len(self.items) == 0:
            return

        op = self.op.split(' ')
        self.inspections += 1
        if op[1] == '*':
            if op[2] == 'old':
                self.items[0] = self.items[0] * self.items[0]
            else:
                self.items[0] *= int(op[2])
        else:
            if op[2] == 'old':
                self.items[0] += self.items[0]
            else:
                self.items[0] += int(op[2])

        # self.items[0] = self.items[0] // 3
        self.items[0] = self.items[0] % (3*11*7*2*19*5*17*13)  # (23*19*13*17)

    def throw(self):
        if len(self.items) == 0:
            return

        if self.items[0] % self.test == 0:
            monkies[self.true_act].items.append(self.items.pop(0))
        else:
            monkies[self.false_act].items.append(self.items.pop(0))


monkies = []

# monkies.append(Monkey(items=[79, 98], op='old * 19',
#                test=23, true_act=2, false_act=3))
# monkies.append(Monkey(items=[54, 65, 75, 74],
#                op='old + 6', test=19, true_act=2, false_act=0))
# monkies.append(Monkey(items=[79, 60, 97], op='old * old',
#                test=13, true_act=1, false_act=3))
# monkies.append(Monkey(items=[74], op='old + 3',
#                test=17, true_act=0, false_act=1))

monkies.append(Monkey(items=[56, 56, 92, 65, 71, 61, 79],
               op='old * 7', test=3, true_act=3, false_act=7))
monkies.append(Monkey(items=[61, 85], op='old + 5',
               test=11, true_act=6, false_act=4))
monkies.append(Monkey(items=[54, 96, 82, 78, 69],
               op='old * old', test=7, true_act=0, false_act=7))
monkies.append(Monkey(items=[57, 59, 65, 95],
               op='old + 4', test=2, true_act=5, false_act=1))
monkies.append(Monkey(items=[62, 67, 80],
               op='old * 17', test=19, true_act=2, false_act=6))
monkies.append(Monkey(items=[91], op='old + 7',
               test=5, true_act=1, false_act=4))
monkies.append(Monkey(items=[79, 83, 64, 52, 77, 56, 63, 92],
               op='old + 6', test=17, true_act=2, false_act=0))
monkies.append(Monkey(items=[50, 97, 76, 96, 80, 56],
               op='old + 3', test=13, true_act=3, false_act=5))

for x in range(10000):  # 20

    for m in monkies:
        for i in range(len(m.items)):
            m.inspect()
            m.throw()

inspections = []
for m in monkies:
    inspections.append(m.inspections)

inspections = sorted(inspections, reverse=True)
i = inspections[0] * inspections[1]
print(i)
# file.close()
