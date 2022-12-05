# Get the data from the test.
import copy
import re
import aoc
orig_data = aoc.get_input(5).splitlines()
stacks = [[], [], [], [], [], [], [], [], []]
instructions = []

bottom = 0
for line in orig_data:
    if line.startswith(' 1 '): break
    bottom += 1

for i in range(bottom-1, -1, -1):
    line = orig_data[i]
    line = line.ljust((4*9)-1)
    for j in range(9):
        char = line[1 + (4*j)]
        if char != ' ': stacks[j].append(char)

for i in range(bottom+2, len(orig_data)):
    line = orig_data[i]
    regex = r"move (\d+?) from (\d) to (\d)"
    matches = re.search(regex, line)
    num = int(matches.group(1))
    src = int(matches.group(2))-1
    dst = int(matches.group(3))-1
    instructions.append((num, src, dst))

def move(inst):
    amt, src, dst = inst
    for _ in range(amt): stacks[dst].append(stacks[src].pop())

def slicemove(inst):
    amt, src, dst = inst
    slice = stacks[src][-amt:]
    stacks[dst].extend(slice)
    for _ in range(amt): stacks[src].pop()

def lasts():
    ret = ""
    for stack in stacks: ret += stack[-1]
    return ret

orig_stacks = copy.deepcopy(stacks)
for inst in instructions: move(inst)
print(f"Answer 1: {lasts()}")

stacks = copy.deepcopy(orig_stacks)
for inst in instructions: slicemove(inst)
print(f"Answer 2: {lasts()}")
