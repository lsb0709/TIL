A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0
b = 0
win = 0

for i in range(10):
    if (A[i] > B[i]):
        a += 3
        win = 1
    elif (A[i] < B[i]):
        b += 3
        win = 1
    else :
        a += 1
        b += 1
print(a, b)

if a > b:
    print('A')

elif b > a:
    print('B')

elif a == b == 10:
    print('D')

else:
    for i in range(1, 11):
        if A[-i] > B[-i]:
            print('A')
            break
        elif A[-i] < B[-i]:
            print('B')
            break
        else:
            continue