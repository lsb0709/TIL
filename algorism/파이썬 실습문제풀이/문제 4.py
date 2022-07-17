# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# 1) while 문
m = 1
total = 1
n = 5
while m <= n:
     total = total * m
     m += 1
print(total)

# 2) for 문
n = 5
total = 1
for i in range(1, n+1):
    total = total * i
print(total)

