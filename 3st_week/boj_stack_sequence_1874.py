def stack_sequence(n, sequence):
    stack = []
    idx = 1
    res = ""
    for num in sequence:
        while idx <= num:
            stack.append(idx)
            idx += 1
            res += "+\n"
        if stack and stack[-1] == num and sequence:
            stack.pop()
            res += "-\n"
        else:
            print("NO")
            return
    print(res)


sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)