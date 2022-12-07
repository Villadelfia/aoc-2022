# Get the data from the test.
import aoc, dpath
orig_data = aoc.get_input(7).splitlines()
data = {}
path = []
paths = set()

for line in orig_data:
    if line.startswith('$'):
        cmd = line[2:]
        if cmd.startswith('cd'):
            target = cmd[3:]
            if target == '/':    path = []
            elif target == '..': path.pop()
            else:                path.append(target)
            if path != []: paths.add('/'.join(path))
    elif not line.startswith('dir'):
        size = int(line.split(' ')[0])
        name = line.split(' ')[1]
        dpath.new(data, '/'.join(path) + '/' + name, size)

def dir_size(data):
    size = 0
    for key in data:
        if type(data[key]) is dict:
            size += dir_size(data[key])
        else:
            size += data[key]
    return size

drive_size = 70000000
free_needed = 30000000
current_free = drive_size - dir_size(data)
need_to_free = free_needed - current_free

total = 0
smallest_deletable = 999999999
for path in paths:
    size = dir_size(dpath.get(data, path))
    if size <= 100000: total += size
    if size >= need_to_free and size < smallest_deletable: smallest_deletable = size

print(f"Answer 1: {total}")
print(f"Answer 2: {smallest_deletable}")
