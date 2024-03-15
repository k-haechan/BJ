# 벌집, 2022년 2월 4일 23:33:27, 30864kb, 72ms, 97b
a=int(input())
i=1
if a==1:
  print(i)
else:
  a-=1 
  while(a>0):
    a-=6*i
    i+=1
  print(i)
