def short_find():
    short = []
    for i in range(9):
        short_input = int(input())
        short.append(short_input)
    short.sort()
    diff = sum(short) - 100

    for i in range(9):
        for j in range(i + 1, 9):
            if short[i] + short[j] == diff:
                short.pop(j)
                short.pop(i)
                for k in range(len(short)):
                    print(short[k])
                return

short_find()