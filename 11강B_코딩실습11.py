줄스타일 = input('각 단을 구분하는 줄 모양을 입력하세요: ')

출력값 = ''

for 앞수 in range(2, 10):
    for 뒷수 in range(1, 10):
        지금값 = '{}x{}={}\n'.format(앞수, 뒷수, 앞수*뒷수)
        출력값 += 지금값

    if 앞수 == 9:
        pass
    else:
        출력값 += 줄스타일 + '\n'

print(출력값)
