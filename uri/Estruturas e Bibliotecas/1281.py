n = int(input())

for _ in range(n):
    x = int(input())
    stock = {}
    result = 0
    for _ in range(x):
        f, v = input().split()
        stock[f] = float(v)
    y = int(input())
    for _ in range(y):
        f, q = input().split()
        result += int(q) * stock[f]
    print("R$ {:.2f}".format(result))
