#!/usr/bin/env python3

w = input().strip().encode()


def xs(g):
    n = next(g, -1)
    return n ^ xs(g) if n >= 0 else 0


def k(d, r=1):
    m, p, s = list(range(256)), 0, 0
    for _ in range(r):
        for i in d:
            for o in range(i//2):
                a, b = (p+o) % 256, (p+i-o-1) % 256
                m[a], m[b] = m[b], m[a]
            p += i + s
            s += 1
    return ''.join(format(xs(m[16*i+j] for j in range(16)), '08b') for i in range(16))


g = [k(list(b'%s-%d' % (w, i)) + [17, 31, 73, 47, 23], 64) for i in range(128)]
print(sum(r.count('1') for r in g))

v = set()


def c(x, y):
    if 0 <= min(x, y) <= max(x, y) < 128 and (x, y) not in v and g[y][x] == '1':
        v.add((x, y))
        for (x, y) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            c(x, y)
        return True


print(sum(1 for x in range(128) for y in range(128) if c(x, y)))
