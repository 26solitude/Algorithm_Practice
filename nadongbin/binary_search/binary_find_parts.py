import sys


def binary_search(arr, n, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == n:
            return True
        elif arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return False


n = int(sys.stdin.readline().rstrip())
store_arr = list(map(int, sys.stdin.readline().rstrip().split()))
store_arr.sort()

m = int(sys.stdin.readline().rstrip())
request_arr = list(map(int, sys.stdin.readline().rstrip().split()))

for request in request_arr:
    if binary_search(store_arr, request, 0, len(store_arr) - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')
