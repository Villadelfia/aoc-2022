# Get the data from the test.
import aoc
orig_data = aoc.get_input(9).splitlines()
head_pos = (0, 0)
tail_pos = (0, 0)
instructions = []
positions = set()
rope_positions = set()
rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

for line in orig_data:
    instruction = line.split(' ')
    direction = instruction[0]
    amount = int(instruction[1])
    for i in range(amount):
        instructions.append(direction)

def drag(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    # If head and tail are touching.
    if head == tail or (abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1):
        return tail

    # Head shares y axis with tail.
    elif head_y == tail_y:
        if head_x > tail_x: tail_x += 1
        else:               tail_x -= 1

    # Head shares x axis with tail.
    elif head_x == tail_x:
        if head_y > tail_y: tail_y += 1
        else:               tail_y -= 1

    # Otherwise do a diagonal jump.
    else:
        if head_x > tail_x: tail_x += 1
        else:               tail_x -= 1
        if head_y > tail_y: tail_y += 1
        else:               tail_y -= 1

    return (tail_x, tail_y)

def do_move(dir):
    global head_pos
    global tail_pos
    global rope

    # motion of the head
    head_x, head_y = head_pos
    if dir == 'U': head_y -= 1
    if dir == 'D': head_y += 1
    if dir == 'L': head_x -= 1
    if dir == 'R': head_x += 1
    head_pos = (head_x, head_y)
    rope[0] = head_pos

    # Drag simple rope
    tail_pos = drag(head_pos, tail_pos)

    # Drag complex rope
    for i in range(9):
        h = rope[i]
        t = rope[i+1]
        t = drag(h, t)
        rope[i+1] = t

    positions.add(f"{tail_pos[0]},{tail_pos[1]}")
    rope_positions.add(f"{rope[9][0]},{rope[9][1]}")

for dir in instructions: do_move(dir)

print(f"Answer 1: {len(positions)}")
print(f"Answer 2: {len(rope_positions)}")
