n = int(input())
words = []

for i in range(n):
    words.append(input())


def check_palindrome(word, count):
    start_index = 0
    end_index = len(word) - 1
    while start_index <= end_index:
        if word[start_index] != word[end_index]:
            count += 1
            if count >= 2:
                return 1
            twice_word1 = word[start_index:end_index]
            twice_word2 = word[start_index + 1:end_index + 1]
            if check_palindrome(twice_word1, count) == 0 or check_palindrome(twice_word2, count) == 0:
                return 1
            else:
                return 2
        start_index += 1
        end_index -= 1
    return 0


for word in words:
    print(check_palindrome(word, 0))
