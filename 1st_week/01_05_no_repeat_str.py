from collections import Counter

def find_not_repeating_first_character(string):
    alphabet = [0] * 26
    for char in string:
        alphabet[ord(char)-ord('a')] += 1

    non_repeat = []
    for i in range(len(alphabet)):
        if alphabet[i] == 1:
            non_repeat.append(chr(i + ord('a')))

    string_list = list(string)
    for char in string_list:
        if char in non_repeat:
            return char
    return "_"

# def find_not_repeating_first_character(string):
#     string_list = list(string)
#     counter = Counter(string)
#     filtered = [key for key in string_list if counter[key] == 1]
#
#     if filtered:
#         return filtered[0]
#     else:
#         return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
