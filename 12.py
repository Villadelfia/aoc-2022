# Get the data from the test.
import queue
import numpy as np
import aoc
orig_data = aoc.get_input(12).splitlines()
heightmap = []
begin_pos = (0, 0)
end_pos = (0, 0)
low_positions = []

y = 0
for line in orig_data:
    m = []
    x = 0
    for char in line:
        if char == 'S':
            m.append(0)
            begin_pos = (x, y)
        elif char == 'E':
            m.append(25)
            end_pos = (x, y)
        else:
            m.append(ord(char) - ord('a'))
        x += 1
    heightmap.append(m)
    y += 1
heightmap = np.array(heightmap)
min_x = 0
min_y = 0
max_x = heightmap.shape[1] - 1
max_y = heightmap.shape[0] - 1

for x in range(max_x+1):
    for y in range(max_y+1):
        if heightmap[y, x] == 0:
            low_positions.append((x, y))

def find_shortest_path(current, end):
    q = queue.SimpleQueue()
    d = queue.SimpleQueue()
    v = set()
    v.add(current)
    q.put(current)
    d.put(0)
    while not q.empty():
        c = q.get()
        depth = d.get()
        if c == end: return depth
        cur_x, cur_y = c
        cur_z = heightmap[cur_y, cur_x]
        if cur_x > min_x:
            l_pos = (cur_x-1, cur_y)
            l_z = heightmap[cur_y, cur_x-1]
            if l_z-1 <= cur_z and l_pos not in v:
                v.add(l_pos)
                q.put(l_pos)
                d.put(depth+1)
        if cur_x < max_x:
            r_pos = (cur_x+1, cur_y)
            r_z = heightmap[cur_y, cur_x+1]
            if r_z-1 <= cur_z and r_pos not in v:
                v.add(r_pos)
                q.put(r_pos)
                d.put(depth+1)
        if cur_y > min_y:
            u_pos = (cur_x, cur_y-1)
            u_z = heightmap[cur_y-1, cur_x]
            if u_z-1 <= cur_z and u_pos not in v:
                v.add(u_pos)
                q.put(u_pos)
                d.put(depth+1)
        if cur_y < max_y:
            d_pos = (cur_x, cur_y+1)
            d_z = heightmap[cur_y+1, cur_x]
            if d_z-1 <= cur_z and d_pos not in v:
                v.add(d_pos)
                q.put(d_pos)
                d.put(depth+1)

print(f"Answer 1: {find_shortest_path(begin_pos, end_pos)}")

res = []
for pos in low_positions:
    len = find_shortest_path(pos, end_pos)
    if len is not None: res.append(len)
res.sort()
print(f"Answer 2: {res[0]}")
