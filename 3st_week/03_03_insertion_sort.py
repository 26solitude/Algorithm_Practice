input = [4, 6, 2, 9, 1]


# def insertion_sort(array):
#     ans = []
#     for num in array:
#         ans.append(num)
#         len_ans = len(ans)
#         while len_ans > 1:
#             if ans[len_ans-1] < ans[len_ans - 2]:
#                 ans[len_ans-1], ans[len_ans - 2] = ans[len_ans - 2], ans[len_ans-1]
#                 len_ans -= 1
#             else:
#                 break
#
#     return ans

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        index = i - 1

        while index >= 0 and array[index] > key:
            array[index + 1] = array[index]
            index -= 1

        array[index + 1] = key

    return array


# insertion_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ", insertion_sort([5, 8, 4, 7, 7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", insertion_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", insertion_sort([100, 56, -3, 32, 44]))
