# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#    total += number
# count += 1

# print(total // count)

# 원인
# 1. count가 for문 밖에 있어서 for문으로 돌지 않기 때문에 1 고정 값을 가지게 된다.
# 2. count를 for문 안으로 넣어주고 print 안에 total / count 나누기 연산자로 바꿔준다.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1
print(total / count)