# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 

n = 'word'
m = ['a','e','i','o','u']
cnt = 0
for i in n :
    for j in m:
        if i == j:
            cnt += 1
print(cnt)