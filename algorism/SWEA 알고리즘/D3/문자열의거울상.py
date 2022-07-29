T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test in range(1, T + 1):
        
        str_ = input()
        str = str_[::-1]
        
        result = ''
        for i in range(len(str)):
            if str[i] == 'q':
                result += 'p'
            elif str[i] == 'p':
                result += 'q'
            elif str[i] == 'd':
                result += 'b'
            else:
                result += 'd'
        print(f'#{test} {result}')