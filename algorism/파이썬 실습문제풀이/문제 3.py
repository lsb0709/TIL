# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# 1) while 문 사용
m = 0
total = 0
n = 10
while m <= n:
    total += m
    m += 1
print(total) 

# 2) for 문 사용
n = 10
cnt = 0
for i in range(1, n+1):
    cnt += i
print(cnt)