fibo = {
    0: 0,
    1: 1
}


def find_fibo(n):
    if n in fibo:
        return fibo[n]

    fibo[n] = find_fibo(n - 1) + find_fibo(n - 2)
    return fibo[n]


n = int(input())
print(find_fibo(n))
