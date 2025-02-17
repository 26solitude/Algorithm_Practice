input = "abcabcabcabcdededededede"


def string_compression(string):
    string_len = len(string)

    for i in range(1, len(string) // 2):
        first_word = string[:i]
        compare_len = 0
        count = 0
        for j in range(i, len(string), i):
            compare_word = string[j:j + i]
            if first_word != compare_word:
                if count != 0:
                    compare_len += 1 + len(first_word)
                else:
                    compare_len += len(first_word)
                count = 0
                first_word = compare_word
            else:
                count += 1

        if count != 0:
            compare_len += 1 + len(first_word)
        else:
            compare_len += len(first_word)

        if compare_len < string_len:
            string_len = compare_len

    return string_len


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))
