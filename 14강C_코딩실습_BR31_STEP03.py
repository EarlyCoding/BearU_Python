게임수 = 0

while True:
    
    A선택 = int(input('A(1~3)?'))

    for n in range(A선택):
        print('A',게임수 + n + 1, '!')
    
    게임수 += A선택
    
    if 게임수 >= 31:
        print('A 벌칙 당첨')
        break

    
    B선택 = int(input('B(1~3)?'))

    for n in range(B선택):
        print('B',게임수 + n + 1, '!')
    
    게임수 += B선택
    
    if 게임수 >= 31:
        print('B 벌칙 당첨')
        break