상덕버거 = int(input())
중덕버거 = int(input())
하덕버거 = int(input())
콜라 = int(input())
사이다 = int(input())

상콜 = 상덕버거 + 콜라 - 50
중콜 = 중덕버거 + 콜라 - 50
하콜 = 하덕버거 + 콜라 - 50
상사 = 상덕버거 + 사이다 - 50
중사 = 중덕버거 + 사이다 - 50
하사 = 하덕버거 + 사이다 - 50

print(min(상콜, 중콜, 하콜, 상사, 중사, 하사))