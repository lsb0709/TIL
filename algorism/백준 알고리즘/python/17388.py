import sys
sys.stdin = open("17388.txt")

S, K, H = map(int, input().split())

if (S + K + H) >= 100 :
    print('OK')

if (S + K + H) < 100 :
    if min(S, K, H) == S:
        print('Soongsil')
    if min(S, K, H) == K:
        print('Korea')
    if min(S, K, H) == H:
        print('Hanyang')