input = [4, 6, 2, 9, 1]


def selection_sort(array):
    len_array = len(array)
    for i in range(len_array - 1):
        index = i
        for j in range(i + 1, len_array):
            if array[index] > array[j]:
                index = j
        array[i], array[index] = array[index], array[i]
    return array


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ", selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", selection_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", selection_sort([100, 56, -3, 32, 44]))
