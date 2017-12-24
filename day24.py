#!/usr/bin/env python3

import sys

d = [tuple(int(y) for y in x.strip().split('/')) for x in sys.stdin.readlines()]


def build(start, rem):
    yield []
    for left, right in rem:
        if start in (left, right):
            subrem = rem[:]
            subrem.remove((left, right))
            x = right if left == start else left
            for rest in build(x, subrem):
                yield [(left, right)] + rest


print(max(sum(l+r for (l, r) in b) for b in build(0, d)))
print(max((len(b), sum(l+r for (l, r) in b)) for b in build(0, d))[1])
