moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

coord = input()
x = ord(coord[0]) - ord('a') + 1
y = int(coord[1])
count = 0

for dx, dy in moves:
    nx, ny = x + dx, y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
