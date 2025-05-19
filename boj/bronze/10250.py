t = int(input())

ans = []

for _ in range(t):
    h, w, n = map(int, input().split())
    rem = n % h
    if rem == 0:
        floor = h
        index = n // h
    else:
        floor = rem
        index = n // h + 1
    ans.append(f"{floor}{index:02d}")

print('\n'.join(ans))
