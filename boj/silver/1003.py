import sys

input = sys.stdin.readline

t = int(input())

fibo = [[0, 0] for _ in range(41)]

fibo[0] = [1, 0]
fibo[1] = [0, 1]

for i in range(2, 41):
    fibo[i][0] = fibo[i - 1][0] + fibo[i - 2][0]
    fibo[i][1] = fibo[i - 1][1] + fibo[i - 2][1]

for _ in range(t):
    n = int(input())
    a, b = fibo[n]
    print(a, b)
