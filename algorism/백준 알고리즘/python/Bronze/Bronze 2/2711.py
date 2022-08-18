T = int(input())

for i in range(1, T+1):
    a, b = input().split()
    a = int(a)
    print(b[:a-1] + b[a::])