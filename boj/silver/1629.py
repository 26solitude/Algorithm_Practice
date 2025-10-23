import sys

a, b, c = map(int, sys.stdin.readline().split())

result = 1

while b > 0:
    if b % 2 == 1:
        result = (result * a) % c
    a = (a * a) % c
    b //= 2

print(result)
