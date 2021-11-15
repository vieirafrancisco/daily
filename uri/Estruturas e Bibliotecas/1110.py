while True:
    x = int(input())

    if x == 0:
        break
    
    deleted = []
    stack = [i for i in range(1, x+1)]

    while len(stack) > 1:
        deleted.append(stack.pop(0))
        stack.append(stack.pop(0))
    
    print(f"Discarded cards: {', '.join(map(str, deleted))}")
    print(f"Remaining card: {stack[0]}")
