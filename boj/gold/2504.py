input_brackets = input()
brackets = list(input_brackets)

stack = []

for bracket in brackets:
    if bracket in '([':
        stack.append(bracket)
    elif bracket in ')]':
        temp = 0
        while stack and stack[-1] not in '([':
            temp += stack.pop()
        if not stack:
            break

        if stack[-1] == '(' and bracket == ')':
            stack.pop()
            if temp:
                stack.append(temp * 2)
            else:
                stack.append(2)
        elif stack[-1] == '[' and bracket == ']':
            stack.pop()
            if temp:
                stack.append(temp * 3)
            else:
                stack.append(3)

if '(' in stack or '[' in stack:
    print(0)
else:
    print(sum(stack))
