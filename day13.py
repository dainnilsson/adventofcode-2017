#!/usr/bin/env python3

import sys, itertools

ls = dict([int(y) for y in x.strip().split(': ')] for x in sys.stdin.readlines())
h = lambda d: [i*ls[i] for i in ls if (i+d) % (ls[i]*2-2) == 0]

print(sum(h(0)))
print(next(d for d in itertools.count(0) if not h(d)))
