# def find_max_occurred_alphabet(string):
#     alphabet = [0] * 26
#     for i in string:
#         if i.isalpha():
#             alphabet[ord(i) - ord('a')] += 1
#
#     max = alphabet[0]
#     index = 0
#     for i in range(len(alphabet)):
#         if alphabet[i] > max:
#             max = alphabet[i]
#             index = i
#
#     return chr(index+ord('a'))


from collections import Counter


def find_max_occurred_alphabet(string):
    string = [char for char in string if char.isalpha()]

    counter = Counter(string)
    print(counter)

    return max(counter, key=counter.get)


result = find_max_occurred_alphabet

print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
