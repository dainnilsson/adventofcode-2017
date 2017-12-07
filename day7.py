#!/usr/bin/env python3

import sys, re

d = [x.strip() for x in sys.stdin.readlines()]

t = dict((m[0], (int(m[1]), m[3].split(', ') if m[3] else []))
         for m in [re.match('(\w+) \((\d+)\)( -> ((\w+, )*\w+))?', l).groups()
                   for l in d])
n = (set(t) - set(c for n in t for c in t[n][1])).pop()
print(n)

w = lambda n: t[n][0] + sum(w(c) for c in t[n][1])
b = lambda n: len({w(c) for c in t[n][1]}) == 1
a = lambda n: sum(w(c) for c in t[n][1]) / len(t[n][1])

while not b(n):
    c = sorted(t[n][1], key=lambda c: -abs(w(c)-a(n)))
    n = ([c for c in t[n][1] if not b(c)] + c)[0]
print(t[c[0]][0] + w(c[1]) - w(c[0]))
