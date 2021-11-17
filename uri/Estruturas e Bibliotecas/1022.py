def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def solve(n1, d1, op, n2, d2):
    if op == "+":
        x = n1*d2 + n2*d1
        y = d1*d2
    elif op == "-":
        x = n1*d2 - n2*d1
        y = d1*d2
    elif op == "/":
        x = n1*d2
        y = n2*d1
    elif op == "*":
        x = n1*n2
        y = d1*d2
    return x, y

n = int(input())

for _ in range(n):
    n1, _, d1, op, n2, _, d2  = input().split()
    x, y = solve(int(n1), int(d1), op, int(n2), int(d2))
    m = mdc(x, y)
    print("{}/{} = {}/{}".format(x, y, x//m, y//m))
