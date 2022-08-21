matrix = []
length = []

for _ in range(5):
    matrix.append(input())
    length.append(len(matrix))

result = ''

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            result += matrix[j][i]

print(result)