import sys

input = sys.stdin.readline

n = int(input())

first_l, first_m, first_r = map(int, input().split())

min_l, min_m, min_r = first_l, first_m, first_r
max_l, max_m, max_r = first_l, first_m, first_r

for _ in range(n - 1):
    now_l, now_m, now_r = map(int, input().split())
    min_l, min_m, min_r = min(min_l, min_m) + now_l, min(min_l, min_m, min_r) + now_m, min(min_m, min_r) + now_r
    max_l, max_m, max_r = max(max_l, max_m) + now_l, max(max_l, max_m, max_r) + now_m, max(max_m, max_r) + now_r

print(max(max_l, max_m, max_r), min(min_l, min_m, min_r))
