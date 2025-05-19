import sys

input = sys.stdin.readline
n = int(input())
# arr = []
#
# for _ in range(n):
#     arr.append(int(input()))
#
# arr.sort()
# for i in arr:
#     print(i)

MAX = 10001

arr = [0] * MAX
for _ in range(n):
    input_num = int(input())
    arr[input_num] += 1

for i in range(1, MAX):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
