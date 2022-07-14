# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

n = 'word'
cnt = 0
for i in n:
    if i == 'a':
        print(cnt)
        break
    cnt += 1
else :
    print(-1)

# 추가문제
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

n = 'HappyHacking'
cnt = 0
for i in n:
    if i == 'a':
        print(cnt, end = ' ')
    cnt += 1