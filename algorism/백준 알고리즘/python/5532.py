L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

result = 0
result1 = 0

a = (A // C)
b = (B // D)
c = (A % C)
d = (B % D)

if a > b:
    result += a
elif a < b:
    result += b

if c or d > 1:
    result1 += 1

print(L - (result + result1))
