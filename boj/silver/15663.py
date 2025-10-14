import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * n


def dfs(sen):
    if len(sen) == m:
        print(*sen)
        return

    prev_num = 0

    for i in range(len(arr)):
        if not visited[i] and arr[i] != prev_num:
            visited[i] = True
            sen.append(arr[i])

            dfs(sen)

            visited[i] = False
            sen.pop()
            prev_num = arr[i]


dfs([])
