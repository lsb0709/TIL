T = int(input())
S = map(int,input().split())
v = int(input())

cnt = 0
for i in S:
    if v == i:
        cnt += 1
print(cnt)