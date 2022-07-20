# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)
T = int(input())

for test in range(1, T+1):
    numbers = list(map(int, input().split()))
    avg = sum(numbers) / len(numbers)
    avg = round(avg)
    print(f'#{test} {avg}')

