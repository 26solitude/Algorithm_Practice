q = []
n, k = map(int, input().split())

for i in range(1, n + 1):
    q.append(i)

res = []
index = k - 1
while True:
    res.append(str(q.pop(index)))
    if not q:
        break
    index = (index + k - 1) % len(q)

print(f"<{", ".join(res)}>")
