# 배수와 약수, 2022년 1월 26일 15:30:23, 30860kb, 68ms, 171b
while(True):
  a,b=map(int,input().split())
  if(a==b):
    break
  if(a%b == 0):
    print("multiple")
  elif(b%a == 0):
    print("factor")
  else:
    print("neither")

