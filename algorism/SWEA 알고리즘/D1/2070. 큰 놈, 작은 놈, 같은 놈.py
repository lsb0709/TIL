# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.

T = int(input())

for test in range(1, T+1):
    a, b = map(int, input().split())
    if a > b :
        result = '>'
    if a == b :
        result = '='
    if a < b:
        result = '<'
    print(f"#{test} {result}")