shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


# def get_max_discounted_price(prices, coupons):
#     prices.sort()
#     coupons.sort()
#
#     res = 0
#
#     while prices and coupons:
#         price = prices.pop()
#         coupon = coupons.pop()
#         res += price - int(price * (coupon * 0.01))
#
#     for price in prices:
#         res += price
#
#     return res

def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    total = 0

    for price, coupon in zip(prices, coupons):
        discount = price * (coupon * 0.01)
        total += price - round(discount)

    total += sum(prices[len(coupons):])

    return total


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
