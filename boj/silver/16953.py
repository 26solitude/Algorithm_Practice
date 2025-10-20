# import sys
# from collections import deque
#
# a, b = map(int, sys.stdin.readline().split())
# count = 1
#
# q = deque([(a, count)])
# checkValid = False
#
# while q:
#     a, count = q.popleft()
#     if a == b:
#         checkValid = True
#         break
#
#     a1 = a * 2
#     a2 = int(str(a) + '1')
#     if a1 <= b:
#         q.append((a1, count + 1))
#     if a2 <= b:
#         q.append((a2, count + 1))
#
# if checkValid:
#     print(count)
# else:
#     print(-1)

import sys

a, b = map(int, sys.stdin.readline().split())
count = 1

while a < b:
    if b % 10 == 1:
        b = b // 10
        count += 1
    elif b % 2 == 0:
        b = b // 2
        count += 1
    else:
        count = -1
        break

if b == a:
    print(count)
else:
    print(-1)
