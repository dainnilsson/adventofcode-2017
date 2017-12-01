#!/usr/bin/env python3

data = input().strip()

ds = [int(d) for d in data]
n = len(ds)

print(sum(d for i, d in enumerate(ds) if d == ds[(i+1) % n]))
print(sum(d for i, d in enumerate(ds) if d == ds[(i+n//2) % n]))
