from collections import deque


def catch_me(c, b):
    time = 0
    queue = deque()
    queue.append((b, 0))
    visited = [{} for _ in range(200001)]

    while c < 200000:
        c += time
        if time in visited[c]:
            return time

        for i in range(0, len(queue)):
            cur_pos, cur_time = queue.popleft()

            new_time = cur_time + 1

            new_pos = cur_pos * 2
            if new_pos < 200001 and new_time not in visited[new_pos]:
                visited[new_pos][new_time] = True
                queue.append((new_pos, new_time))

            new_pos = cur_pos + 1
            if new_pos < 200001 and new_time not in visited[new_pos]:
                visited[new_pos][new_time] = True
                queue.append((new_pos, new_time))

            new_pos = cur_pos - 1
            if new_pos >= 0 and new_time not in visited[new_pos]:
                visited[new_pos][new_time] = True
                queue.append((new_pos, new_time))

        time += 1


print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))
