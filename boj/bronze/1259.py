while True:
    n = str(input())
    if n == "0":
        break
    check = True
    for i in range(0, len(n) // 2):
        if n[i] != n[-i - 1]:
            check = False
            break
    if check:
        print("yes")
    else:
        print("no")
