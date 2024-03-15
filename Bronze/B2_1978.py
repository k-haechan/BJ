# 소수 찾기, 2022년 2월 8일 11:34:55, 30860kb, 68ms, 197b
def pn(p):
  if p==1: return False
  i=2
  while i*i<=p:
    if p%i==0:
      return False
    i+=1
  return True

l=int(input())
a=list(map(int,input().split()))
c=len(list(filter(pn,a)))
print(c)
