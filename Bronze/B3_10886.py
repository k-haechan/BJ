# 0 = not cute / 1 = cute, 2022년 1월 26일 15:01:13, 30864kb, 72ms, 160b
t,f=0,0
for _ in range(int(input())):
  if(int(input())==0):
    f+=1
  else:
    t+=1
if(t<f):
  print("Junhee is not cute!")
else:
  print("Junhee is cute!")

