#!/usr/bin/env python3

import sys


def tick(m, cx, cy, dx, dy, dc):
    c = m.get((cx, cy), 0)
    s = c % 4
    dx, dy = (dy, -dx) if s == 0 else (-dy, dx) \
        if s == 2 else (-dx, -dy) if s == 3 else (dx, dy)
    m[(cx, cy)] = c + dc
    return cx + dx, cy + dy, dx, dy


m, w, h = {}, 0, 0
for y, line in enumerate(sys.stdin.readlines()):
    for x, c in enumerate(line.strip()):
        m[(x, y)] = int(c == '#')*2
        w, h = max(w, x), max(h, y)

start = sum(c // 4 + (c % 4) // 2 for c in m.values())

ma = dict(m)
dx, dy, cx, cy = 0, -1, w // 2, h // 2
for _ in range(10000):
    cx, cy, dx, dy = tick(ma, cx, cy, dx, dy, 2)
print(sum((c // 4) + ((c % 4) // 2) for c in ma.values()) - start)

dx, dy, cx, cy = 0, -1, w // 2, h // 2
for _ in range(10000000):
    cx, cy, dx, dy = tick(m, cx, cy, dx, dy, 1)
print(sum((c // 4) + ((c % 4) // 2) for c in m.values()) - start)
