data = []

for i in range(1, 6):
    T = input()

    if 'FBI' in T:
        data.append(i) # FBI가 존재하는 i번째만 data저장

if data:
    print(*data)

else :
    print("HE GOT AWAY!")