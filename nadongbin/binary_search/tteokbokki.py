def cutting(tteoks, cut_height):
    return sum(tteok - cut_height for tteok in tteoks if tteok > cut_height)


def binary_search(tteoks, start, end, m):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if cutting(tteoks, mid) >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


n, m = map(int, input().split())
tteoks = list(map(int, input().split()))

print(binary_search(tteoks, 0, max(tteoks), m))
