#!/usr/bin/env python3

import sys

states = {}
state = input()[-2]
iterations = int(input().split()[-2])


def parse(lines):
    lines.pop(0)
    w = 0 if '0' in lines.pop(0) else 1
    m = -1 if 'left' in lines.pop(0) else 1
    s = lines.pop(0)[-2]
    return (w, m, s)


lines = [x.strip() for x in sys.stdin.readlines()]
while lines:
    assert not lines.pop(0)  # Empty line
    key = lines.pop(0)[-2]
    states[key] = (parse(lines), parse(lines))

cursor = 0
tape = {}
for _ in range(iterations):
    tape[cursor], m, state = states[state][tape.get(cursor, 0)]
    cursor += m

print(sum(tape.values()))
