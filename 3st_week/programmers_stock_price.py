from collections import deque


def solution(prices):
    answer = []

    queue = deque(prices)
    while queue:
        num = queue.popleft()
        idx = 0
        for i in queue:
            idx += 1
            if num > i:
                break
        answer.append(idx)

    return answer


prices = [1, 2, 3, 2, 3]
print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", solution(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", solution([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", solution([1, 5, 3, 6, 7, 6, 5]))
