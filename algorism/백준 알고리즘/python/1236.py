# 영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다. 
# 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.

# 성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에는 성의 상태가 주어진다. 성의 상태는 .은 빈칸, X는 경비원이 있는 칸이다.

# 출력
# 첫째 줄에 추가해야 하는 경비원의 최솟값을 출력한다.

n, m = map(int, input().split())

# matrix = [list(map(str, input())) for _ in range(n)] # 리스트 컴프리헨션

matrix = []
for _ in range(n):
    line = list(map(str, input()))
    matrix.append(line)

cnt_row = 0
cnt_column = 0
for i in range(n):
    if 'X' not in matrix[i]: # 행에 X가 없으면 1 추가
        cnt_row += 1

for j in range(m):
    if ['X' not in matrix[i][j] for i in range(n)]: # 열에 X가 없으면 1 추가
            cnt_column += 1

print(max(cnt_row, cnt_column))