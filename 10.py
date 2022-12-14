# Get the data from the test.
import aoc
orig_data = aoc.get_input(10).splitlines()
cur_x = 1
x_vals = []

for line in orig_data:
    if line == 'noop':
        x_vals.append(cur_x)
    else:
        x_vals.append(cur_x)
        x_vals.append(cur_x)
        cur_x += int(line.split(' ')[1])

def sig_str(i):
    return x_vals[i-1] * i

print(f"Answer 1: {sig_str(20) + sig_str(60) + sig_str(100) + sig_str(140) + sig_str(180) + sig_str(220)}")

print("Answer 2:")
for y in range(6):
    for x in range(40):
        i = (y*40) + x
        x_val = x_vals[i]
        if abs(x_val-x) <= 1: print('#', end='')
        else:                 print(' ', end='')
    print()
