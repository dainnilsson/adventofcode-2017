#!/usr/bin/env python3

import sys

data = [[int(x) for x in row.split()] for row in sys.stdin.readlines()]

print(sum(max(r)-min(r) for r in data))
print(sum(x//y for r in data for x in r for y in r if x != y and x % y == 0))
