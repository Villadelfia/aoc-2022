import numpy as np
import matplotlib.pyplot as plt
import aoc
orig_data = aoc.get_input(14).splitlines()
cave = np.zeros((1000, 200))

# Draw walls.
maxy = 0
for path in orig_data:
    points = path.split(' -> ')
    points = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in points]
    for x in range(len(points)-1):
        x_s = points[x][0]
        y_s = points[x][1]
        x_e = points[x+1][0]
        y_e = points[x+1][1]
        x_s, x_e = sorted([x_s, x_e])
        y_s, y_e = sorted([y_s, y_e])
        maxy = sorted([maxy, y_s, y_e])[2]
        if x_s == x_e: cave[x_s, y_s:y_e+1] = 2
        if y_s == y_e: cave[x_s:x_e+1, y_s] = 2
cave[0:1000, maxy+2] = 2

#Drop sand
sand = (500, 0)
sx, sy = sand
a1given = False
while True:
    blocked = True
    for next in [(0, 1), (-1, 1), (1, 1)]:
        nx, ny = next
        if cave[sx+nx, sy+ny] == 0:
            sx += nx
            sy += ny
            blocked = False
            break
    if sy >= maxy and not a1given:
        print(f"Answer 1: {sum(1 for x in cave.flatten() if x == 1)}")
        a1given = True
    if blocked:
        cave[sx, sy] = 1
        if (sx, sy) == sand:
            print(f"Answer 2: {sum(1 for x in cave.flatten() if x == 1)}")
            break
        sx, sy = sand

plt.matshow(cave.transpose())
plt.colorbar()
plt.show()
