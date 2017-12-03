#!/usr/bin/env python3

from math import sqrt
data = int(input().strip())


def pos(index):
    s = int(sqrt(index-1))
    if s % 2 == 0:
        s -= 1
    i = index - s*s - 1
    if i < s:
        return ((s+1)//2, i-s//2)
    i -= s
    if i < s + 2:
        return (1+s//2-i, s//2+1)
    i -= (s+2)
    if i < s:
        return (-s//2, s//2-i)
    i -= s
    return (i-s//2-1, -s//2)


print(sum(abs(c) for c in pos(data)))

mem = {(0, 0): 1}
largest = 1
i = 2
while largest <= data:
    x, y = pos(i)
    s = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            adj = (x+a, y+b)
            s += mem.get(adj, 0)
    mem[(x, y)] = largest = s
    i += 1
print(largest)
