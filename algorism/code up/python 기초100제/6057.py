a, b = map(int, input().split())

print((bool(not a and not b)) or (bool(a and b)))