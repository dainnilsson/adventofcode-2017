#!/usr/bin/env python3

import sys, math

d = [x.strip().split() for x in sys.stdin.readlines()]


def v(mem, x):
    try:
        return int(x)
    except ValueError:
        return mem.get(x, 0)


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def tick(i):
    ins, a, b = d[i]
    b = v(m, b)
    if ins == 'set':
        m[a] = b
    elif ins == 'sub':
        m[a] = v(m, a) - b
    elif ins == 'mul':
        m[a] = v(m, a) * b
    elif ins == 'jnp':
        if not is_prime(v(m, a)):
            i += b - 1
    elif v(m, a):
        i += b - 1
    return i + 1


m, i, mul = {}, 0, 0
while 0 <= i < len(d):
    if d[i][0] == 'mul':
        mul += 1
    i = tick(i)
print(mul)

d[8] = 'jnp b 17'.split()
d[9] = 'jnz 1 17'.split()
m, i = {'a': 1}, 0
while 0 <= i < len(d):
    i = tick(i)
print(m['h'])
