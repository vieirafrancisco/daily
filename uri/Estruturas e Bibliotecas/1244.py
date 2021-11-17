n = int(input())

for _ in range(n):
    arr = input().split()
    print(" ".join(sorted(arr, reverse=True, key=len)))
