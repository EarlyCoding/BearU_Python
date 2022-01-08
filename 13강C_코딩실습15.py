print('Mutable(Changable, 주소가 변경될 수 있는) 자료형 주소 출력하기')
숫자 = 90
print(id(숫자))

숫자 = 100
print(id(숫자))

print('-' * 10)
print('Immutable(Changable, 주소가 변경되지 않는) 자료형 주소 출력하기')
리스트 = [1, 2, 3]
print(리스트)
print(id(리스트))

리스트[2] =6
print(리스트)
print(id(리스트))