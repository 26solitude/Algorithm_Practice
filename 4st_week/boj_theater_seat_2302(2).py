memo = {
    1: 1,
    2: 2
}


def fibo(n, memo):
    if n == 0:
        return 1
    
    if n in memo:
        return memo[n]

    nth_fibo = fibo(n - 1, memo) + fibo(n - 2, memo)
    memo[n] = nth_fibo
    return nth_fibo


n = int(input())
seat_num = int(input())
vip_seats = []
for i in range(seat_num):
    vip_seats.append(int(input()))

answer = 1
now_index = 0
for vip_seat in vip_seats:
    vip_index = vip_seat - 1
    seat_range = vip_index - now_index
    answer *= fibo(seat_range, memo)
    now_index = vip_index + 1
answer *= fibo(n - now_index, memo)

print(answer)
