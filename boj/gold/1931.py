import sys

input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

start = 0
result = 0

for meeting in meetings:
    if start <= meeting[0]:
        start = meeting[1]
        result += 1

print(result)
