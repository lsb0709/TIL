A, B = map(int, input().split())

M = (B - A) / 400

S = 1 / (1 + 10 ** M)

print(S)

