# import sys

# sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

for test in range(1, T+1):

    E = str(input())

    list = ''
    
    for i in E:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            list += i


    print(f'#{test} {list}')