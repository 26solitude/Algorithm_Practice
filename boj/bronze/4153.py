import sys

input = sys.stdin.readline


# ans = []
# while True:
#     arr = list(map(int, input().split()))
#     if all(x == 0 for x in arr):
#         break
#     arr.sort()
#     if arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2]:
#         ans.append("right")
#     else:
#         ans.append("wrong")
#
# print("\n".join(ans))

def is_right(a: int, b: int, c: int) -> bool:
    x, y, z = sorted((a, b, c))
    return x * x + y * y == z * z


while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    print("right" if is_right(a, b, c) else "wrong")
