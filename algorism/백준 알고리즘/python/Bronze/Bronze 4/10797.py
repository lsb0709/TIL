N = input()

S = list(map (str, input().split()))

cnt = 0

for i in S:
    if i == N :
        cnt += 1

print(cnt)