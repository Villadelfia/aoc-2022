# Get the data from the test.
import aoc
orig_data = aoc.get_input(4).splitlines()
ranges = []

for line in orig_data:
    r1 = line.split(',')[0]
    r2 = line.split(',')[1]
    r1 = range(int(r1.split('-')[0]), int(r1.split('-')[1]))
    r2 = range(int(r2.split('-')[0]), int(r2.split('-')[1]))
    ranges.append((r1, r2))

def contains(r1, r2):
    if r1.start <= r2.start and r1.stop >= r2.stop: return 1
    if r2.start <= r1.start and r2.stop >= r1.stop: return 1
    return 0

def overlaps(r1, r2):
    if r1.start <= r2.start and r1.stop >= r2.start: return 1
    if r2.start <= r1.start and r2.stop >= r1.start: return 1
    return 0

print(f"Answer 1: {sum([contains(x[0], x[1]) for x in ranges])}")
print(f"Answer 1: {sum([overlaps(x[0], x[1]) for x in ranges])}")
