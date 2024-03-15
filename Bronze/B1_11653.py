# 소인수분해, 2022년 1월 25일 11:29:48, 30864kb, 1456ms, 88b
N=int(input()); d=2

while(N!=1):
  if((N%d)==0):
    N/=d
    print(d)
  else:
    d+=1
