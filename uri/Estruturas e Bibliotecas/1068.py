def is_correct_expr(expr):
    stack = list()
    for char in expr:
        if char == ")" and len(stack) == 0:
            return False

        if char == "(":
            stack.append(char)
        elif char == ")":
            stack.pop()
    return len(stack) == 0


while True:
    try:
        e = input()
        result = is_correct_expr(e)
        if result:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break
