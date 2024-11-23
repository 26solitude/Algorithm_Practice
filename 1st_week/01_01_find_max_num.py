arr1 = [3, 5, 6, 1, 2, 4]
arr2 = [33, 125, 6, 221, 52, 11, 454]
arr3 = [243, 5, 6, 1, 2332, 421]


# def find_max(num_arr):
#     for num in num_arr:
#         is_max_num = True
#         for compare_num in num_arr:
#             if num < compare_num:
#                 is_max_num = False
#         if is_max_num:
#             return num

# def find_max(num_arr):
#     max = num_arr[0]
#     for num in num_arr:
#         if num > max: max = num
#     return max

def find_max(num_arr):
    return max(num_arr)


print(find_max(arr1))
print(find_max(arr2))
print(find_max(arr3))
