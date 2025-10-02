import sys, heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    q = []
    q_rev = []
    nums = {}

    k = int(input())

    for _ in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            nums[num] = nums.get(num, 0) + 1
            heapq.heappush(q, num)
            heapq.heappush(q_rev, -num)
        elif op == 'D':
            if num == 1 and q_rev:
                while q_rev and nums[-q_rev[0]] <= 0:
                    heapq.heappop(q_rev)
                if q_rev:
                    v = heapq.heappop(q_rev)
                    nums[-v] -= 1
            elif num == -1 and q:
                while q and nums[q[0]] <= 0:
                    heapq.heappop(q)
                if q:
                    v = heapq.heappop(q)
                    nums[v] -= 1

    while q_rev and nums[-q_rev[0]] <= 0:
        heapq.heappop(q_rev)
    while q and nums[q[0]] <= 0:
        heapq.heappop(q)
    if not q:
        print("EMPTY")
    else:
        print(-heapq.heappop(q_rev), heapq.heappop(q))
