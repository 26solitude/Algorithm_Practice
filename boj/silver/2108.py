from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

a = sum(arr) // n
arr.sort()
b = arr[n//2]
counter = Counter(arr)
c = counter.most_common()
d = max(arr) - min(arr)

print(a, b, c, d)
