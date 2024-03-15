# 화성 수학, 2022년 1월 24일 22:51:22, 30860kb, 72ms, 236b
n=int(input())

def afs(a):
  s=float(a[0])
  for i in range(1,len(a)):
    if(a[i]=='@'):
      s*=3      
    elif(a[i]=='%'):
      s+=5
    else:
      s-=7
  return s

for i in range(n):
 
  a=input().split()
  print('%.2f'%afs(a))
