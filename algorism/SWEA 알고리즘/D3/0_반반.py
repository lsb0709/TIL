# import sys

# sys.stdin = open("_반반.txt")

TC = int(input())

for i in range(1, TC+1):
    S = str(input())
    matrix = []
    for j in S:
        matrix.append(j)
    matrix.sort()

    # if matrix[0] == matrix[1] and matrix[2] == matrix[3] and matrix[1] != matrix[2]:
    #     result1 = 'Yes'
    #     #print('Yes')
    
    # else :
    #     reuslt2 = 'No'
    #     #print('No')

    # print(f'#{i} {??}')
    
    print("#{} {}".format(i, 'Yes' if matrix[0] == matrix[1] and matrix[2] == matrix[3] and matrix[1] != matrix[2] 
    else 'No'))