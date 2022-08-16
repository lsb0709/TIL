a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

M = max((a+b+c),(a+b+d),(b+c+d),(c+d+a))
N = max(e, f)

print(M + N)

# arr = []
# for _ in range(6):
#     arr.append(int(input()))

# max_four = sorted(arr[:4])
# min_two = arr[4:]

# print(sum(max_four[1:]) + max(min_two))
