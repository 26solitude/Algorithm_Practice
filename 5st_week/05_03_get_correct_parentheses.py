from collections import deque

balanced_parentheses_string = "()))((()"


def check_balance(string):
    stack = []
    for chr in string:
        if chr == '(':
            stack.append(chr)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


def divide_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = ''.join(list(queue))
    return u, v


def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == "":
        return ""

    u, v = divide_u_v(balanced_parentheses_string)
    if check_balance(u):
        return u + get_correct_parentheses(v)
    else:
        v_string = '(' + get_correct_parentheses(v) + ')'
        u = u[1:-1]
        u_string = ""
        for chr in u:
            if chr == '(':
                u_string += ')'
            else:
                u_string += '('
        return v_string + u_string


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))
