# 윤년, 2022년 1월 25일 21:00:05, 30864kb, 68ms, 100b
S=int(input())
if(S%4==0 and S%100!=0):
  print("1")
elif(S%400==0):
  print("1")
else:
  print("0")
