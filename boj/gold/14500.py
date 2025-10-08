import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# square_max_sum = -2e19
# horizontal_max_sum = -2e19
# vertical_max_sum = -2e19
#
# for i in range(n - 1):
#     for j in range(m - 1):
#         square_sum = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
#         if square_sum > square_max_sum:
#             square_max_sum = square_sum
#
# for i in range(n):
#     for j in range(m - 3):
#         horizontal_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
#         if horizontal_sum > horizontal_max_sum:
#             horizontal_max_sum = horizontal_sum
#
# for i in range(n - 3):
#     for j in range(m):
#         vertical_sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
#         if vertical_sum > vertical_max_sum:
#             vertical_max_sum = vertical_sum
#
# print(horizontal_max_sum, vertical_max_sum)

visited = [[False for _ in range(m)] for _ in range(n)]
max_sum = -2e19

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, depth, current_sum):
    global max_sum
    if depth == 4:
        max_sum = max(max_sum, current_sum)
        return

    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            dfs(next_x, next_y, depth + 1, current_sum + arr[next_x][next_y])
            visited[next_x][next_y] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False

valid_max_sum = -2e19
for i in range(n):
    for j in range(m):
        all_neighbors = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
        center_val = arr[i][j]
        valid_neighbors = [arr[nx][ny] for nx, ny in all_neighbors if 0 <= nx < n and 0 <= ny < m]

        if len(valid_neighbors) == 3:
            current_sum = center_val + sum(valid_neighbors)
            max_sum = max(max_sum, current_sum)
        elif len(valid_neighbors) == 4:
            for neighbor in valid_neighbors:
                current_sum = center_val + sum(valid_neighbors) - neighbor
                max_sum = max(max_sum, current_sum)

print(max_sum)
