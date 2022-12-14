# Get the data from the test.
from copy import deepcopy
import aoc
orig_data = aoc.get_input(11).split('\n\n')
monkeys = []

class Monkey:
    def __init__(self, id, items, operator, operand, test, if_true, if_false):
        self.id = id
        self.items = items
        self.operator = operator
        self.operand = operand
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.business_count = 0
        self.modulo = 0

    def do_business(self, round=1):
        result = []
        for item in self.items:
            self.business_count += 1
            if self.operator == '^': item *= item
            if self.operator == '+': item += self.operand
            if self.operator == '*': item *= self.operand
            if round == 1: item = item // 3
            else:          item = item % self.modulo
            if item % self.test == 0: result.append((self.if_true, item))
            else:                     result.append((self.if_false, item))
        self.items = []
        return result

    def recv_business(self, business):
        for act in business:
            if act[0] == self.id: self.items.append(act[1])

modulo = 1
for data in orig_data:
    data = data.splitlines()
    id = int(data[0].split(' ')[1][0:-1])
    items = data[1].split(':')[1].split(',')
    items = [int(x[1:]) for x in items]
    op = data[2].split('= ')[1]
    operator = None
    operand = None
    if op == 'old * old':
        operator = '^'
    elif '+' in op:
        operator = '+'
        operand = int(op.split('+ ')[1])
    elif '*' in op:
        operator = '*'
        operand = int(op.split('* ')[1])
    test = int(data[3].split(' ')[-1])
    if_true = int(data[4].split(' ')[-1])
    if_false = int(data[5].split(' ')[-1])
    monkeys.append(Monkey(id, items, operator, operand, test, if_true, if_false))
    modulo *= test

# For part 2 to not explode in time and memory, we do do the lcm of all the divisors.
for monkey in monkeys: monkey.modulo = modulo

original = deepcopy(monkeys)
for i in range(20):
    for monkey in monkeys:
        business = monkey.do_business()
        for receiver in monkeys:
            receiver.recv_business(business)

business = [x.business_count for x in monkeys]
business.sort()
print(f"Answer 1: {business[-2] * business[-1]}")

monkeys = original
for i in range(10000):
    for monkey in monkeys:
        business = monkey.do_business(2)
        for receiver in monkeys:
            receiver.recv_business(business)

business = [x.business_count for x in monkeys]
business.sort()
print(f"Answer 2: {business[-2] * business[-1]}")
