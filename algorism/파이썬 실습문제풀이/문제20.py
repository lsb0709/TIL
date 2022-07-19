# 문제 20. 각 자릿수의 합 구하기

# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

number = 123
result = 0

while number: #0 일 때 반복문을 종료해 주기 위한 조건
    result += number % 10
    number // 10
print(result)