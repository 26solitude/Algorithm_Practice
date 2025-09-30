import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

ladder = {}
snake = {}

for _ in range(n):
    start, end = map(int, input().split())
    ladder[start] = end

for _ in range(m):
    start, end = map(int, input().split())
    snake[start] = end

cube = [0] * 101

q = deque([1])
going = True
count = 0

while going:
    for _ in range(len(q)):
        idx = q.popleft()

        if idx == 100:
            print(count)
            going = False
            break

        for i in range(1, 7):
            next_idx = idx + i
            if next_idx <= 100 and cube[next_idx] == 0:
                if next_idx in snake.keys():
                    cube[snake[next_idx]] = 1
                    q.append(snake[next_idx])
                elif next_idx in ladder.keys():
                    cube[ladder[next_idx]] = 1
                    q.append(ladder[next_idx])
                else:
                    cube[next_idx] = 1
                    q.append(next_idx)
    if not going:
        break
    count += 1
