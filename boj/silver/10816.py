# n = int(input())
# row, col = 2, 100000001
# arr = [[0] * col for _ in range(row)]
#
# arrA = list(map(int, input().split()))
# for i in arrA:
#     if i >= 0:
#         arr[0][i] += 1
#     else:
#         arr[1][abs(i)] += 1
#
# m = int(input())
# arrB = list(map(int, input().split()))
#
# result = " ".join(str(arr[0][x]) if x >= 0 else str(arr[1][abs(x)]) for x in arrB)
#
# print(result)

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arrA = list(map(int, input().split()))
counts = Counter(arrA)

m = int(input())
arrB = list(map(int, input().split()))

print(" ".join(str(counts[x]) for x in arrB))
