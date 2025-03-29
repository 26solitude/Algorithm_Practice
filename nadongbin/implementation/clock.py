n = int(input())
count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # time = str(i) + str(j) + str(k)
            # if time.find('3') != -1:
            #     count += 1
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
