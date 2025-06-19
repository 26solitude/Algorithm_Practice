import sys

input = sys.stdin.readline

S = set()
m = int(input())
for _ in range(m):
    input_v = input().split()
    op = input_v[0]
    if len(input_v) == 2:
        v = int(input_v[1])

        if op == "add" and v not in S:
            S.add(v)
        elif op == "remove" and v in S:
            S.remove(v)
        elif op == "check":
            print("1" if v in S else "0")
        elif op == "toggle":
            if v in S:
                S.remove(v)
            else:
                S.add(v)
    else:
        if op == "all":
            S = set(range(1, 21))
        elif op == "empty":
            S = set()
