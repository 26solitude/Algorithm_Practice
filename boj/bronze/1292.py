start, end = map(int, input().split())
arr = []
num = 1

while True:
    for _ in range(num):
        arr.append(num)
    num += 1
    if len(arr) > end:
        break

print(sum(arr[start - 1:end]))
