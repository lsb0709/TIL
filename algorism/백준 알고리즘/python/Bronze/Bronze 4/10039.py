total = 0

for i in range(5):
    T = int(input())

    if T < 40:
        T = 40
    total += T

print(total // 5)