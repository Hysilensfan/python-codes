def operation(g: str) -> int:
    stack: list = []
    for token in input().split():
        if token.isdigit():  # Is a digit, push the number.
            stack.append(int(token))
        else:  # Else get 2 digits, then operating.
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
    return stack[0]


[print(operation(input())) for _ in range(int(input()))]
