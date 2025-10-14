import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

sen = []


def dfs(start):
    if len(sen) == m:
        print(*sen)
        return

    for i in range(start, len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            sen.append(arr[i])
            dfs(i)
            sen.pop()


dfs(0)
