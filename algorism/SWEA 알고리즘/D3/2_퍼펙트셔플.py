# import sys

# sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
    
for i in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))

    if len(card) % 2 == 0:
        ss = 0
        
