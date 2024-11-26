input1 = "011110"
input2 = "11111"
input3 = "00000001"
input4 = "11001100110011000001"
input5 = "11101101"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_zero = 0
    count_to_one = 0

    if string[0] == "0":
        count_to_one += 1
    elif string[0] == "1":
        count_to_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_one += 1
            if string[i + 1] == '1':
                count_to_zero += 1
    return min(count_to_one, count_to_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one
print(result(input1))
print(result(input2))
print(result(input3))
print(result(input4))
print(result(input5))
