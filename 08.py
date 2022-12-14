# Get the data from the test.
import aoc
import numpy as np
orig_data = aoc.get_input(8).splitlines()
height_matrix = []

for line in orig_data:
    row = []
    for char in line:
        row.append(int(char))
    height_matrix.append(row)
height_matrix = np.array(height_matrix)

def visible(x, y):
    if x == 0 or y == 0 or x == 98 or y == 98: return 1
    el = height_matrix[x, y]
    if el > max(height_matrix[x, :y]): return 1
    if el > max(height_matrix[x, y+1:]): return 1
    if el > max(height_matrix[:x, y]): return 1
    if el > max(height_matrix[x+1:, y]): return 1
    return 0

def scenic_score(x, y):
    el = height_matrix[x, y]
    score_left = 0
    score_right = 0
    score_up = 0
    score_down = 0
    for i in range(1,99):
        if x-i < 0: break
        score_left += 1
        if height_matrix[x-i, y] >= el: break
    for i in range(1,99):
        if x+i > 98: break
        score_right += 1
        if height_matrix[x+i, y] >= el: break
    for i in range(1,99):
        if y-i < 0: break
        score_up += 1
        if height_matrix[x, y-i] >= el: break
    for i in range(1,99):
        if y+i > 98: break
        score_down += 1
        if height_matrix[x, y+i] >= el: break
    return score_down*score_left*score_right*score_up

visible_amt = 0
for x in range(99):
    for y in range(99):
        visible_amt += visible(x, y)

print(f"Answer 1: {visible_amt}")

max_score = 0
for x in range(99):
    for y in range(99):
        score = scenic_score(x,y)
        if score > max_score: max_score = score

print(f"Answer 2: {max_score}")
