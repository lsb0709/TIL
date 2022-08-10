a = int(input())
b = int(input())
c = int(input())

sum = (a + b + c)

if a and b and c == 60:
    print('Equilateral')
if sum == 180 and a == b or a == c or b == c :
    print('Isosceles')
if sum == 180 and a != b != c :
    print('Scalene')
if sum != 180:
    print('Error')