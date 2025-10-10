import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

visited = [False for _ in range(n)]


def dfs(result):
    if len(result) == m:
        print(*result)
        return

    for i in range(len(arr)):
        if visited[i]:
            continue

        result.append(arr[i])
        visited[i] = True
        dfs(result)
        result.pop()
        visited[i] = False


dfs([])
