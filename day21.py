#!/usr/bin/env python3

import sys


def parse(x):
    return [[int(c == '#') for c in l] for l in x.split('/')]


def rot(g):
    for _ in range(4):
        g = list(zip(*g[::-1]))
        yield g


def key(g):
    return str(min(min(x, x[::-1]) for x in rot(g)))


def iterate(g):
    s = 2 + len(g) % 2
    return sum([list(zip(*sum(r, [])))
                for r in [[m[key([[c for c in l[x:x+s]]
                                  for l in g[y:y+s]])]
                           for x in range(0, len(g), s)]
                          for y in range(0, len(g), s)]], [])


m = {}
for line in sys.stdin.readlines():
    k, r = [parse(x) for x in line.strip().split(' => ')]
    m[key(k)] = r

s = parse('.#./..#/###')

for _ in range(5):
    s = iterate(s)
print(sum(1 for r in s for c in r if c))

for _ in range(18-5):
    s = iterate(s)
print(sum(1 for r in s for c in r if c))
