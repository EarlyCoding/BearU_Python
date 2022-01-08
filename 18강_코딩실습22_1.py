import time

class 오른쪽으로달리기:

    def __init__(self, 나의이름):
        self.이동거리 = 나의이름 + ':'
    
    def 달리기(self):
        for 숫자 in range(0, 100):
            self.이동거리 = self.이동거리 + '*'
            print(self.이동거리)

수호 = 오른쪽으로달리기('수호')
세훈 = 오른쪽으로달리기('세훈')

수호.달리기()
세훈.달리기()
