import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = list(input().strip())
    n = int(input())
    arr_str = input().strip()
    if n == 0:
        arr = []
    else:
        arr = list(map(int, arr_str[1:-1].split(',')))

    left = 0
    right = n - 1
    isReversed = False
    isError = False

    for op in p:
        if op == 'R':
            isReversed = not isReversed
        elif op == 'D':
            if left > right:
                isError = True
                break

            if isReversed:
                right -= 1
            else:
                left += 1

    if isError:
        print("error")
    else:
        result = arr[left:right + 1]
        if isReversed:
            result.reverse()
        print('[' + ','.join(map(str, result)) + ']')
