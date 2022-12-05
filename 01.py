# Get the data from the test.
import aoc
orig_data = aoc.get_input(1).splitlines()
data = []
work = []

# More convenient format.
for line in orig_data:
    if line == "":
        data.append(work)
        work = []
    else:
        work.append(int(line))
data.append(work)

# Sum subsequences and sort results.
sums = [sum(x) for x in data]
sums.sort()

# Answer 1 = max.
print(f"Answer to part 1: {sums[-1]}")

# Answer 2 = three highest.
print(f"Answer to part 2: {sum(sums[-3:])}")
