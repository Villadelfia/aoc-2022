# Get the data from the test.
import aoc
orig_data = aoc.get_input(6)

for i in range(0, len(orig_data)-4):
    s = set(orig_data[i:i+4])
    if len(s) == 4:
        print(f"Answer 1: {i+4}")
        break

for i in range(0, len(orig_data)-14):
    s = set(orig_data[i:i+14])
    if len(s) == 14:
        print(f"Answer 2: {i+14}")
        break
