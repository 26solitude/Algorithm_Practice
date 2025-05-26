# import heapq
#
# n = int(input())
# arr = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     heapq.heappush(arr, (x, y))
#
# while arr:
#     x, y = heapq.heappop(arr)
#     print(x, y)

import sys

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

out = '\n'.join(f"{x} {y}" for x, y in arr)
sys.stdout.write(out)
