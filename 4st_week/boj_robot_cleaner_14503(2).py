n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for i in range(n):
    room.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate_dir(direction):
    return (direction + 3) % 4


answer = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1

    moved = False
    for i in range(4):
        d = rotate_dir(d)
        dr = r + dx[d]
        dc = c + dy[d]
        if room[dr][dc] == 0:
            r, c = dr, dc
            moved = True
            break

    if not moved:
        back_d = (d + 2) % 4
        dr = r + dx[back_d]
        dc = c + dy[back_d]

        if room[dr][dc] == 1:
            break
        else:
            r, c = dr, dc

print(answer)
