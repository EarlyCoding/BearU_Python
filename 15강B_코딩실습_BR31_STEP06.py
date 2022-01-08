import random

게임수 = 0

while True:

    while True:
        try:
            A선택 = int(input('A(1~3)?'))
            
            if A선택 == 1 or A선택 == 2 or A선택 == 3:   
                break
            else:
                print('[경고]1,2,3 숫자만 입력하세요!')
        except:
            print('[경고]숫자만 입력하세요!')
        
    for n in range(A선택):
        print('A',게임수 + n + 1, '!')
    
    게임수 += A선택
    
    if 게임수 >= 31:
        print('A 벌칙 당첨')
        break

    
    B선택 = random.randint(1,3)

    for n in range(B선택):
        print('컴',게임수 + n + 1, '!')
    
    게임수 += B선택
    
    if 게임수 >= 31:
        print('컴 벌칙 당첨')
        break