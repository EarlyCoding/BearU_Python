import threading

class 오른쪽으로달리기(threading.Thread):

   def __init__(self,나의이름):
       threading.Thread.__init__(self)
       self.이동거리 = 나의이름 + ':'
  
   def run(self):
       for 숫자 in range(0, 200):
           self.이동거리 = self.이동거리 + '*'
           print(self.이동거리)

수호 = 오른쪽으로달리기('수호')
세훈 = 오른쪽으로달리기('세훈')

수호.start()
세훈.start()
