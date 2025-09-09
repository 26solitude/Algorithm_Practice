import heapq, sys

input = sys.stdin.readline

max_heap = []
min_heap = []

n = int(input())

for i in range(n):
    x = int(input())
    if x < 0:
        heapq.heappush(max_heap, -x)
    elif x > 0:
        heapq.heappush(min_heap, x)
    else:
        if max_heap:
            if min_heap and max_heap[0] > min_heap[0]:
                print(heapq.heappop(min_heap))
            else:
                print(-heapq.heappop(max_heap))
        else:
            if min_heap:
                print(heapq.heappop(min_heap))
            else:
                print(0)
