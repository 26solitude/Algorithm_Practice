people_count = 0
max = 0
for i in range(10):
    outpeople, inpeople = map(int, input().split())
    people_count = people_count - outpeople + inpeople
    if max < people_count:
        max = people_count

print(max)
