import sys

n = int(sys.stdin.readline().rstrip())
store_arr = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
request_arr = list(map(int, sys.stdin.readline().rstrip().split()))

results = []
for request_item in request_arr:
    results.append("yes" if request_item in store_arr else "no")
print(" ".join(results))

# for request_item in request_arr:
#     if request_item in store_arr:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')
