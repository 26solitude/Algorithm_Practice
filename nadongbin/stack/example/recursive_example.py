def recursive_function(n):
    if n == 10:
        return
    print(n, '번째 재귀 함수에서', n + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(n + 1)
    print(n, '번째 재귀 함수를 종료합니다.')


recursive_function(0)
