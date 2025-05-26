# stack = []
#
# n = int(input())
#
# for _ in range(n):
#     command = input().split()
#     if len(command) == 1:
#         if command[0] == 'pop':
#             if len(stack) == 0:
#                 print(-1)
#             else:
#                 print(stack.pop(0))
#         elif command[0] == 'size':
#             print(len(stack))
#         elif command[0] == 'empty':
#             if len(stack) == 0:
#                 print(1)
#             else:
#                 print(0)
#         elif command[0] == 'front':
#             if len(stack) == 0:
#                 print(-1)
#             else:
#                 print(stack[0])
#         elif command[0] == 'back':
#             if len(stack) == 0:
#                 print(-1)
#             else:
#                 print(stack[len(stack) - 1])
#     else:
#         if command[0] == 'push':
#             stack.append(command[1])

import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
result = []

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        result.append(queue.popleft() if queue else '-1')
    elif command[0] == 'size':
        result.append(str(len(queue)))
    elif command[0] == 'empty':
        result.append('0' if queue else '1')
    elif command[0] == 'front':
        result.append(queue[0] if queue else '-1')
    elif command[0] == 'back':
        result.append(queue[len(queue) - 1] if queue else '-1')

out = "\n".join(result)
print(out)
