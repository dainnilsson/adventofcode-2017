#!/usr/bin/env python3

import sys, math

d = [x.strip().split() for x in sys.stdin.readlines()]


def v(mem, x):
    try:
        return int(x)
    except ValueError:
        return mem.get(x, 0)


m = {}
i = 0
cmul = 0
while 0 <= i < len(d):
    ins, a, b = d[i]
    b = v(m, b)
    if ins == 'set':
        m[a] = b
    elif ins == 'sub':
        m[a] = v(m, a) - b
    elif ins == 'mul':
        m[a] = v(m, a) * b
        cmul += 1
    elif v(m, a):
        i += b - 1
    i += 1

print(cmul)

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

print(sum(1 for b in range(106500, 123501, 17) if not is_prime(b)))
