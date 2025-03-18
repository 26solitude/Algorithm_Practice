import math


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


n, k = map(int, input().split())

print(math.gcd(n, k))
print(math.lcm(n, k))
