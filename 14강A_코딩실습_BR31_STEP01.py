게임수 = 0

while True:
    
    나의선택 = int(input('A(1~3)?'))
    
    게임수 += 나의선택
    
    if 게임수 >= 31:
        break

print('벌칙 당첨')