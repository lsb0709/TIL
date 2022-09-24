T = int(input())

cups = [1, 2, 3]
for i in range(T):
    x, y = map(int, input().split())

    x1 = cups.index(x)
    y1 = cups.index(y)

    cups[x1], cups[y1] = cups[y1], cups[x1]

print(cups[0])