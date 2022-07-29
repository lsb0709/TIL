T = int(input())

for test in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))

    avg = sum(M) / N
    cnt = 0

    for i in M:
        if i <= avg:
            cnt += 1
    print(f'#{test} {cnt}')