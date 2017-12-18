#!/usr/bin/env python3

import sys

d = [x.strip().split() for x in sys.stdin.readlines()]


def v(mem, x):
    try:
        return int(x)
    except ValueError:
        return mem.get(x, 0)

def g(q_in, q_out, x=0):
    reg = {'p': q_in.pop(0)}
    i = 0
    while 0 <= i < len(d):
        ins = d[i]
        c = ins[0]
        a = v(reg, ins[1])
        if c == 'snd':
            q_out.append(a)
        elif c == 'rcv':
            if x:
                if a:
                    yield q_out[-1]
                    return
            elif not q_in:
                yield None
            reg[ins[1]] = q_in.pop(0)
        else:
            b = v(reg, ins[2])
            if c == 'set':
                reg[ins[1]] = b
            elif c == 'add':
                reg[ins[1]] = a + b
            elif c == 'mul':
                reg[ins[1]] = a * b
            elif c == 'mod':
                reg[ins[1]] = a % b
            elif c == 'jgz' and a > 0:
                i += b - 1
        i += 1


print(next(g([0], [], 1)))

aq, bq = [0], [1]
a = g(aq, bq)
b = g(bq, aq)
z = 0

while aq:
    if aq:
        try:
            next(a)
        except:
            aq = None
    if bq:
        try:
            next(b)
        except:
            break
        finally:
            z += len(aq)
print(z)
