import sys
from collections import deque

input = sys.stdin.readline

t = int(input())


def calc_dslr(n):
    d = (n * 2) % 10000
    s = (10000 + n - 1) % 10000
    l = (n * 10) % 10000 + (n * 10) // 10000
    r = (n % 10) * 1000 + n // 10
    return d, s, l, r


for _ in range(t):
    a, b = map(int, input().split())
    q = deque([a])
    visited = [None] * 10001
    visited[a] = (-1, '')

    while q:
        num = q.popleft()
        if num == b:
            result = []
            while num != a:
                prev_num, op = visited[num]
                result.append(op)
                num = prev_num
            result.reverse()
            print(''.join(result))
            break

        d, s, l, r = calc_dslr(num)
        if visited[d] is None:
            q.append(d)
            visited[d] = (num, 'D')
        if visited[s] is None:
            q.append(s)
            visited[s] = (num, 'S')
        if visited[l] is None:
            q.append(l)
            visited[l] = (num, 'L')
        if visited[r] is None:
            q.append(r)
            visited[r] = (num, 'R')
