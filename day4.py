#!/usr/bin/env python3

import sys

data = [row.split() for row in sys.stdin.readlines()]

print(sum(1 for p in data if len(p) == len(set(p))))
print(sum(1 for p in data if len(p) == len(set([tuple(sorted(w)) for w in p]))))
