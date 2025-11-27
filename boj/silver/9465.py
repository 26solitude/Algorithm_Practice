import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    now_top = arr[0][0]
    now_bot = arr[1][0]

    prev_top = 0
    prev_bot = 0

    for i in range(1, n):
        new_top = max(now_bot, prev_bot) + arr[0][i]
        new_bot = max(now_top, prev_top) + arr[1][i]

        prev_top, prev_bot = now_top, now_bot
        now_top, now_bot = new_top, new_bot

    print(max(now_top, now_bot))
