n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0


def check(row, col, len):
    global white, blue
    first_color = arr[row][col]
    for i in range(row, row + len):
        for j in range(col, col + len):
            if first_color != arr[i][j]:
                half = len // 2
                check(row, col, half)
                check(row + half, col, half)
                check(row, col + half, half)
                check(row + half, col + half, half)
                return
    if first_color == 0:
        white += 1
    else:
        blue += 1


check(0, 0, n)
print(white)
print(blue)
