# 소수, 2022년 2월 8일 12:31:50, 30860kb, 84ms, 263b
def pn(p):
  if p==1: return False
  i=2
  while i*i<=p:
    if p%i==0:
      return False
    i+=1
  return True

a=int(input())
b=int(input())
c=[]
for i in range(a,b+1):
  if pn(i)==True:
    c.append(i)
print("{}\n{}".format(sum(c),c[0]) if len(c)!=0 else -1)
