N = int(input())
s = list(map(int, input().split()))

line = [0] * 101

result = 0

for i in s:
    if line[i] == 0:
        line[i] += 1
    else:
        result += 1

print(result)