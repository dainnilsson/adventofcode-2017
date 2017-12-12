#!/usr/bin/env python3

import sys

ls = [x.strip() for x in sys.stdin.readlines()]
c, g = [[int(x) for x in l.split(' <-> ')[1].split(', ')] for l in ls], set()
tr = lambda i, a: a.union(*[tr(x, a.union([x])) for x in c[i] if x not in a])
print(len(tr(0, g)))
print(len([g.update(tr(i, g)) for i in range(len(c)) if i not in g]))
