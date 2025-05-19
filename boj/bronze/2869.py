import math

a, b, v = map(int, input().split())
# day = 0
# height = 0
#
# while True:
#     height += a
#     day += 1
#     if height >= v:
#         print(day)
#         break
#     height -= b

print(math.ceil((v - b) / (a - b)))
