#!/usr/bin/env python3

e = d = v = i = n = 0
for c in input().strip():
    if d:
        d = 0
    elif c == '!':
        d = 1
    elif n:
        if c == '>':
            n = 0
        else:
            i += 1
    elif c == '{':
        e += 1
    elif c == '<':
        n = 1
    elif c == '}':
        v += e
        e -= 1

print(v)
print(i)
