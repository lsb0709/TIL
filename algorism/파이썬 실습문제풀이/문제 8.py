# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100, 40]
max_number = numbers[0]
secound_number = numbers[0]
for n in numbers :
    if max_number < n :
        secound_number = max_number
        max_number = n
    elif secound_number < n and n < max_number:
        secound_number = n
print(secound_number)
