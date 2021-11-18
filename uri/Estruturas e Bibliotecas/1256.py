n = int(input())

def solve(value):
    s = " -> ".join(value)
    if s:
        return "-> " + s + " ->"
    return "->"

for k in range(n):
    m, c = list(map(int, input().split()))
    _hash = {i: [] for i in range(m)}
    h = lambda x: x % m
    values = list(map(int, input().split()))
    for x in values:
        _hash[h(x)].append(str(x))
    for key, value in _hash.items():
        print("{} {} \\".format(key, solve(value)))
    if k < n-1:
        print("")
