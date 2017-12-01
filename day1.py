#!/usr/bin/env python3

data = input().strip()

ds = [int(d) for d in data]
n = len(ds)

print(sum(ds[i] for i in range(n) if ds[i] == ds[(i+1) % n]))
print(sum(ds[i] for i in range(n) if ds[i] == ds[(i+n//2) % n]))
