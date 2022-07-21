# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.

# (시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)

T = int(input())

for test in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    m = m1 + m2
    h = h1 + h2 + m // 60
    m = m % 60
    if h > 12 :
        h = (h - 12)
    print(f'#{test} {h} {m}')