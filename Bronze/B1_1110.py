# 더하기 사이클, 2022년 1월 28일 22:51:41, 30864kb, 72ms, 184b
a=input()
tmp=int(a)
N=0
while True:#ㄴㄴ do while
  if(len(a)==1):
    a=a*2
    
  else:
    a=a[1]+str((int(a[0])+int(a[1]))%10)
    
  N+=1
  if(int(a)==tmp):
    break

print(N)
