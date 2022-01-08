이름 = input('이름: ')
나이 = int(input('나이: '))

개인정보 = {'이름':이름, '나이':나이}

for 키만 in 개인정보.keys():
    print('- 키: ', 키만)

for 벨류만 in 개인정보.values():
    print('- 값:', 벨류만)

주소 = input('주소: ')
개인정보['주소'] = 주소
print(개인정보)

삭제할키 = input('삭제할 키: ')
개인정보.pop(삭제할키)
print(개인정보)
