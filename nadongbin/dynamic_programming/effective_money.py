n, m = map(int, input().split())
tokens = []
for i in range(n):
    tokens.append(int(input()))

d = [2e19] * (m + 1)

for token in tokens:
    d[token] = 1

for i in range(max(tokens) + 1, m + 1):
    for token in tokens:
        d[i] = min(d[i], d[i - token] + 1)

if d[m] == 2e19:
    print(-1)
else:
    print(d[m])
