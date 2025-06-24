import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = {}

for _ in range(n):
    url, password = map(str, input().split())
    arr[url] = password

for _ in range(m):
    url = input().strip()
    print(arr[url])
