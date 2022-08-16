data = list(map(int, input().split()))

data.sort()

print(abs((data[3] + data[0]) - (data[2] + data[1])))



