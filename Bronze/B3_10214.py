# Baseball, 2022년 1월 27일 13:37:49, 30860kb, 104ms, 213b
for _ in range(int(input())):
  y_s,k_s=0,0
  for _ in range(9):
    y,k=map(int,input().split())
    y_s+=y; k_s+=k
  if(y_s>k_s):
    print("Yonsei")
  elif(y_s<k_s):
    print("Korea")
  else:
    print("Draw")
