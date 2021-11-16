n = int(input())

a = []
b = []

for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        a.append(x)
    else:
        b.append(x)

for x in sorted(a):
    print(x)

for x in sorted(b, reverse=True):
    print(x)
