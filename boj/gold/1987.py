import sys

input = sys.stdin.readline


def solve():
    R, C = map(int, input().split())
    board = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(R)]

    q = {(0, 0, 1 << board[0][0])}
    result = 1

    while q:
        r, c, mask = q.pop()

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C:
                n_bit = 1 << board[nr][nc]
                if not (mask & n_bit):
                    new_mask = mask | n_bit
                    q.add((nr, nc, new_mask))
                    result = max(result, bin(new_mask).count('1'))

    print(result)


solve()
