# 한수, 2022년 1월 31일 22:16:09, 30864kb, 72ms, 284b
def arithSeq(a):
  a=str(a)
  b=int(a[1])-int(a[0])
  for i in range(1,len(a)-1):
    if int(a[i+1])-int(a[i]) != b:
      return 0
  return 1

a=int(input())
if(a<100):
  print(a)
else:
  cnt=99
  for i in range(100,a+1):
    #판별함수
    cnt+=arithSeq(i)
  print(cnt)
    
  

