# 개표, 2022년 1월 26일 14:57:26, 30864kb, 72ms, 171b
n=int(input())
b=input()
NA,NB=0,0

for i in range(n):
  if b[i]=='A':
    NA+=1
  else:
    NB+=1

if(NA==NB):
  print("Tie")
elif(NA>NB):
  print("A")
else:
  print("B")
