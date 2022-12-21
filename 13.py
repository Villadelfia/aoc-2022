import functools
import itertools
import aoc
orig_data = aoc.get_input(13).split('\n\n')
pairs = [(eval(x.split('\n')[0]), eval(x.split('\n')[1])) for x in orig_data]
packets = list(itertools.chain(*pairs))
packets.append([[2]])
packets.append([[6]])

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else (-1 if a < b else 1)
    elif isinstance(a, int):
        return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])
    elif a and b:
        q = compare(a[0], b[0])
        return q if q else compare(a[1:], b[1:])
    return 1 if a else (-1 if b else 0)

packets = sorted(packets, key=functools.cmp_to_key(compare))
print(f"Answer 1: {sum(i + 1 for i, x in enumerate(pairs) if compare(x[0], x[1]) == -1)}")
print(f"Answer 2: {(packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)}")
