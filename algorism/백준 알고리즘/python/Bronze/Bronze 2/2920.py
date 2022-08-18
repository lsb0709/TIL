T = "cdefgabC"

for i in input().split():
    for j in range(len(T)):
        if i == j:
            print('ascending')