#!/usr/bin/env python3

d = int(input().strip())

b, p, n = [0], 0, 0

for i in range(1, 2018):
    p = 1 + (p + d) % i
    b.insert(p, i)
print(b[p+1 % len(b)])

for i in range(1, 50000001):
    p = 1 + (p + d) % i
    if p == 1:
        n = i
print(n)
