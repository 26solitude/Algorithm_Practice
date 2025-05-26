n = int(input())
arrA = set(map(int, input().split()))

m = int(input())
arrB = list(map(int, input().split()))

result = "\n".join("1" if x in arrA else "0" for x in arrB)
print(result)
