import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

count = 0
result = 0

i = 0

while i < m:
    if s[i:i + 3] == 'IOI':
        count += 1
        if count == n:
            result += 1
            count -= 1
        i += 2
    else:
        count = 0
        i += 1

print(result)
