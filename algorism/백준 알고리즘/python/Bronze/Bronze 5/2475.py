T = map(int, input().split())

result = 0
mul = 0
for i in T:
    mul += (i * i)

result = mul % 10
print(result)