a, b, c, d = map(int, input().split())

e, f, g, h = map(int, input().split())

S = (a + b + c + d)

T = (e + f + g + h)

if S > T :
    print(S)

if T > S :
    print(T)

if S == T :
    print(S)