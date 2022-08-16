arr = []
for i in range(9):
    T = int(input())
    arr.append(T)
print(max(arr))
print(arr.index(max(arr))+1)