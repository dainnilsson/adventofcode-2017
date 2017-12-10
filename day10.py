#!/usr/bin/env python3

data = input().strip()


def k(d, r=1):
    m, p, s = list(range(256)), 0, 0
    for _ in range(r):
        for i in d:
            for o in range(i//2):
                a, b = (p+o) % 256, (p+i-o-1) % 256
                m[a], m[b] = m[b], m[a]
            p += i + s
            s += 1
    return m


m = k([int(x) for x in data.split(',')])
print(m[0] * m[1])

m = k(list(data.encode()) + [17, 31, 73, 47, 23], 64)
o = ''
for i in range(0, 256, 16):
    x = 0
    for j in range(16):
        x ^= m[i+j]
    o += '%02x' % x
print(o)
