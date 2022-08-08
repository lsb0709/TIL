T = int(input())
for i in range(1, T+1):
    S = int(input()) # 자동차의 가격
    N = int(input()) # 옵션의 개수

    total = 0
    for j in range(1, N+1):
        q, p = map(int, input().split())
        total += q * p

    print(S + total)