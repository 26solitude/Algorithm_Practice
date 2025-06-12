from collections import deque

t = int(input())

result = []
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque([(i, x) for i, x in enumerate(arr)])

    count = 0
    while queue:
        idx, val = deque.popleft(queue)

        if any(val < other_val for _, other_val in queue):
            queue.append((idx, val))
        else:
            count += 1
            if idx == m:
                result.append(str(count))
                break

print("\n".join(result))
