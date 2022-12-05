# Get the data from the test.
import aoc
orig_data = aoc.get_input(3).splitlines()
common_items = []
badges = []

for line in orig_data:
    p1, p2 = line[:len(line)//2], line[len(line)//2:]
    item = [x for x in p1 if x in p2]
    common_items.append(item[0])

for i in range(0, len(orig_data), 3):
    badge = set(orig_data[i+0]) & set(orig_data[i+1]) & set(orig_data[i+2])
    badges.append(badge.pop())

def priority(item):
    value = ord(item)
    if value >= ord('a') and value <= ord('z'): value = value - ord('a') + 1
    elif value >= ord('A') and value <= ord('Z'): value = value - ord('A') + 27
    return value

print(f"Answer 1: {sum(map(priority, common_items))}")
print(f"Answer 2: {sum(map(priority, badges))}")
