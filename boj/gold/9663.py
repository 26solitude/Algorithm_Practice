import sys

n = int(sys.stdin.readline())
ans = 0


def dfs(row, col_mask, ld_mask, rd_mask):
    global ans
    if row == n:
        ans += 1
        return

    available_bits = ~(col_mask | ld_mask | rd_mask) & ((1 << n) - 1)

    while available_bits > 0:
        pick = available_bits & -available_bits

        dfs(row+1, col_mask|pick, (ld_mask|pick)<<1, (rd_mask|pick)>>1)
        available_bits &= ~pick


dfs(0 ,0,0,0)
print(ans)
