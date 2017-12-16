#!/usr/bin/env python3

d = input().strip().split(',')
s = list('abcdefghijklmnop')
p = s[:]
q = []

while not q or p != s:
    for m in d:
        if m[0] == 's':
            p = p[-int(m[1:]):] + p[:-int(m[1:])]
        else:
            a, b = (int(x) for x in m[1:].split('/')) if m[0] == 'x' else \
                (p.index(x) for x in m[1:].split('/'))
            p[a], p[b] = p[b], p[a]
    q.append(p[:])

print(''.join(q[0]))
print(''.join(q[999999999 % len(q)]))
