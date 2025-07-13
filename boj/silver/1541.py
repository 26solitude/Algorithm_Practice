import sys

sen = sys.stdin.readline().strip()

arr = sen.split("-")
res = sum(int(x) for x in arr.pop(0).split("+"))

for i in arr:
    n = i.split("+")
    n_sum = sum(int(x) for x in n)
    res -= n_sum

print(res)
