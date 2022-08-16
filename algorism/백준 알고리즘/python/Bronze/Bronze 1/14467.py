N = int(input())


dic = {}

cnt = 0

for i in range(N):
    num, location = map(int, input().split())

    if num not in dic:
        dic[num] = location
    
    else: # dic 안에 값과 다른 값이 들어온다면
        if dic[num] != location:
            cnt += 1
            dic[num] = location

print(cnt)