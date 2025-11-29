import sys

input = sys.stdin.readline

A = input().strip()
B = input().strip()

LCS = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[-1][-1])

i, j = len(A), len(B)
result = []

while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:
        result.append(A[i - 1])
        i -= 1
        j -= 1
    else:
        if LCS[i - 1][j] > LCS[i][j - 1]:
            i -= 1
        else:
            j -= 1

print("".join(result[::-1]))
