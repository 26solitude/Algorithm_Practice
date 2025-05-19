n = int(input())
s = input()
sum = 0
for i in range(len(s)):
    num = ((ord(s[i]) - 96) * 31 ** i)
    sum += num
print(sum % 1234567891)
