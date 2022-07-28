# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

T = int(input())

for test in range(1, T+1):
    n = list(map(int, input().split()))
    add = 0
    for i in n :
        if i % 2 == 1:
            add += i
    print(f'#{test} {add}')