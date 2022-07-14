# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
n = 'word'
d = {}
for i in n:
    d[i] = d.get(i, 0) + 1
for key, value in d.items():
    print(key, value)
