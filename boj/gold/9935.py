import sys

s = sys.stdin.readline().strip()
bomb = list(map(str, sys.stdin.readline().strip()))

stack = []

for char in s:
    stack.append(char)
    if len(stack) >= len(bomb) and stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')