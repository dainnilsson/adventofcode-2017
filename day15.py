#!/usr/bin/env python3

import sys
from itertools import islice

d = [int(x.strip().split()[-1]) for x in sys.stdin.readlines()]
a, b = (d[0], 16807, 4), (d[1], 48271, 8)


def g(s, f, m=1):
    while True:
        s = s*f % 2147483647
        if s % m == 0:
            yield s & 0xffff


print(sum(1 for x, y in islice(zip(g(*a[:2]), g(*b[:2])), 40000000) if x == y))
print(sum(1 for x, y in islice(zip(g(*a), g(*b)), 5000000) if x == y))
