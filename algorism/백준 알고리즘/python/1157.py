# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

word = input().upper() # word = mississipi
word_list = list(set(word)) # word_list = ["m", "i", "s", "p"]
cnt = []

for i in word_list :
    count = word.count(i)
    cnt.append(count)  # cnt = [4, 4, 1, 1]

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])