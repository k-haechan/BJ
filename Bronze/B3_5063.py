# TGN, 2022년 1월 26일 14:42:37, 30860kb, 88ms, 198b
n=int(input())
for _ in range(n):
  r,e,c=map(int,input().split())
  rev=e-c-r
  if(rev>0):
    print("advertise")
  elif(rev==0):
    print("does not matter")
  else:
    print("do not advertise")

