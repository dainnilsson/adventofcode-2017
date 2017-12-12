#!/usr/bin/env python3

data = input().strip().split(',')

d = lambda x, y: max(abs(x), (abs(x)+1)//2+abs(y))
x = y = m = 0
for s in data:
    y += 1 if s == 'n' or x % 2 and 'n' in s else -1 if s == 's' or not x % 2 and 's' in s else 0
    x += -1 if 'w' in s else 1 if 'e' in s else 0
    m = max(m, d(x, y))
print(d(x, y))
print(m)
