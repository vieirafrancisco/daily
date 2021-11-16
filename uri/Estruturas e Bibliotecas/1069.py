n = int(input())

for _ in range(n):
    stack = []
    count = 0
    string = input()
    for char in string:
        if char == "<":
            stack.append(char)
        elif char == ">" and len(stack) > 0:
            stack.pop(0)
            count += 1
    print(count)
