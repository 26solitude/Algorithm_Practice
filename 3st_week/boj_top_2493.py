# 5
# 6 9 5 7 4

n = int(input())
arr = list(map(int, input().split()))
res = [0] * n

# for i in range(n - 1, -1, -1):
#     for j in range(i - 1, -1, -1):
#         if arr[i] <= arr[j]:
#             res[i] = j + 1
#             break

# while arr:
#     height = arr.pop()
#     for i in range(len(arr)-1, -1, -1):
#         if arr[i] >= height:
#             res[len(arr)] = i + 1
#             break

stack = []
for i in range(n):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    if stack:
        res[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(map(str, res)))
