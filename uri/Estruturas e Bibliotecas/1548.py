n = int(input())

for _ in range(n):
    x = int(input())
    arr = list(map(int, input().split()))
    print(sum([x==y for x, y in zip(arr, sorted(arr, reverse=True))]))
