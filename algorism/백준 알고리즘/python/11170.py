T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    
    cnt = 0
    for j in (range(N, M+1)): 
        line = str(j) # count 함수를 쓰기위해 str으로 형변환 해준다.(int는 쓸 수 없다.)
        cnt += line.count('0')
    print(cnt)