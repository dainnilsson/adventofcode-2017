#!/usr/bin/env python3

import sys
lines = [x.strip() for x in sys.stdin.readlines()]


def tick(ps):
    for p in ps:
        p['v'] = [sum(x) for x in zip(p['v'], p['a'])]
        p['p'] = [sum(x) for x in zip(p['p'], p['v'])]


ps = [dict([(y[0], [int(z) for z in y[3:-1].split(',')])
            for y in x.split(', ')]) for x in lines]
val = 0
r = 0
while r < 300:
    r += 1
    tick(ps)
    x = min((sum(abs(x) for x in p['p']), i) for i, p in enumerate(ps))[1]
    if val != x:
        val = x
        r = 0
print(val)

ps = [dict([(y[0], [int(z) for z in y[3:-1].split(',')])
            for y in x.split(', ')]) for x in lines]
r = 0
while r < 50:
    r += 1
    i = 0
    while i < len(ps) - 1:
        for j in range(len(ps)-1, i, -1):
            if ps[i]['p'] == ps[j]['p']:
                r = 0
                del ps[j]
        if r:
            i += 1
        else:
            del ps[i]
            r += 1
    tick(ps)
print(len(ps))
