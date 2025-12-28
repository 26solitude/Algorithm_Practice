import sys

lines = sys.stdin.readlines()
nums = list(map(int, lines))

sys.setrecursionlimit(10 ** 6)

idx = 0

def post_order(min_val, max_val):
    global idx

    if idx >= len(nums):
        return

    val = nums[idx]
    if not (min_val < val < max_val):
        return

    idx += 1

    post_order(min_val, val)
    post_order(val, max_val)
    print(val)


post_order(-float('inf'), float('inf'))

# stack = [(0, len(nums) - 1)]
# result = []
#
# while stack:
#     start, end = stack.pop()
#
#     if start > end:
#         continue
#
#     root = nums[start]
#     result.append(root)
#
#     mid = end + 1
#     for i in range(start + 1, end + 1):
#         if nums[i] > root:
#             mid = i
#             break
#     stack.append((start + 1, mid - 1))
#     stack.append((mid, end))
#
# print('\n'.join(map(str, result[::-1])))
