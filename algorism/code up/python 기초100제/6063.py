a, b = map(int, input().split())

if a>=b :
    print(a)
else :
    print(b)

print(a if (a>=b) else b)