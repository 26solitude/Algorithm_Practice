import sys

input = sys.stdin.readline

n = int(input())

board = [[' ' for _ in range(2 * n)] for _ in range(n)]


def stamp_star(r, c):
    board[r][c] = '*'
    board[r + 1][c + 1] = '*'
    board[r + 1][c - 1] = '*'
    for i in range(-2, 3):
        board[r + 2][c + i] = '*'


def make_star(n, r, c):
    if n == 3:
        stamp_star(r, c)
        return

    next_n = n // 2

    make_star(next_n, r, c)
    make_star(next_n, r + next_n, c - next_n)
    make_star(next_n, r + next_n, c + next_n)


make_star(n, 0, n-1)
for row in board:
    print(''.join(row))