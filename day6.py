#!/usr/bin/env python3

d = [int(i) for i in input().strip().split()]

for _ in [0]*2:
    s = set()
    while tuple(d) not in s:
        s.add(tuple(d))
        n = max(d)
        i = d.index(n)
        d[i] = 0
        for j in range(n):
            d[(i+j+1) % len(d)] += 1
    print(len(s))
