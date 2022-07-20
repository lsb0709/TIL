# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

T = int(input())


for test in range(1, T+1):
    num = int(input())

    result = 0
    for i in range(1, num+1):
      if i % 2 == 1:
          result += i
      elif i % 2 == 0:
          result -= i
           
    print(f'#{test} {result}')
