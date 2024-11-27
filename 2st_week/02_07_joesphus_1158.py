N, K = map(int, input().split())
K -= 1

input_list = []
for i in range(1, N + 1):
    input_list.append(i)

cur_index = K
ans = []
while True:
    if len(input_list) == 1:
        ans.append(input_list.pop())
        break
    ans.append(input_list.pop(cur_index))
    cur_index = (cur_index + K) % len(input_list)

result = f"<{', '.join(map(str, ans))}>"
print(result)
