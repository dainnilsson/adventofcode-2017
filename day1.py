#!/usr/bin/env python3

data = input('Enter puzzle input: ').strip()
print()

ds = [int(d) for d in data]
a = sum(ds[i] for i in range(len(ds)) if ds[i] == ds[(i+1) % len(ds)])
b = sum(ds[i] for i in range(len(ds)) if ds[i] == ds[(i+len(ds)//2) % len(ds)])

print('Solutions')
print('Part 1:', a)
print('Part 2:', b)
