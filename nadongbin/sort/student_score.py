n = int(input())
arr = []

for i in range(n):
    name, score = input().split()
    arr.append((name, int(score)))

sorted_arr = sorted(arr, key=lambda student: student[1])

for name, score in sorted_arr:
    print(name, end=' ')
