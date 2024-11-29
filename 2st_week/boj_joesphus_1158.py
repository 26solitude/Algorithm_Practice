# BOJ 1158
def josephus_problem(n, k):
    result_arr = []
    next_index = k - 1

    people_arr = list(range(1, n + 1))
    while people_arr:
        result_arr.append(people_arr.pop(next_index))
        if len(people_arr) != 0:
            next_index = (next_index + k - 1) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep="")


n, k = map(int, input().split())
josephus_problem(n, k)

# from collections import deque
#
# N, K = map(int, input().split())
# K -= 1
#
# input_deque = deque(range(1, N + 1))
# ans = []
#
# while input_deque:
#     input_deque.rotate(-K)
#     ans.append(input_deque.popleft())
#
# result = f"<{', '.join(map(str, ans))}>"
# print(result)
