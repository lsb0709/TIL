# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
#1
a = str(input())

reversed_str = ''

for i in a:
    reversed_str = i + reversed_str
print(reversed_str)

#2
c = a[::-1]

print(c)