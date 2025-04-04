import sys

n = int(sys.stdin.readline().rstrip())
store_input = list(map(int, sys.stdin.readline().rstrip().split()))
store_arr = [0] * 1000000
for store_item in store_input:
    store_arr[store_item] += 1

m = int(sys.stdin.readline().rstrip())
request_arr = list(map(int, sys.stdin.readline().rstrip().split()))

results = []
for request_item in request_arr:
    results.append("yes" if store_arr[request_item] > 0 else "no")
print(" ".join(results))

# for request_item in request_arr:
#     if store_arr[request_item] > 0:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')
