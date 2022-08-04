students = []
for i in range(1, 31):
    students.append(i)

for j in range(28):
    a = int(input())
    students.remove(a)
print(min(students))
print(max(students))