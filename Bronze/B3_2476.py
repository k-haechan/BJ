# 주사위 게임, 2022년 1월 26일 13:31:29, 30860kb, 116ms, 305b
def price(l):
  if(l[0]==l[1]==l[2]):
    return l[0]*1000+10000
  elif(l[0]==l[1] or l[0]==l[2]):
    return l[0]*100+1000
  elif(l[1]==l[2]): return l[1]*100+1000
  else: return max(l)*100 

a=int(input())
m=0
for _ in range(a):
  z=list(map(int,input().split()))
  if(price(z)>m): m=price(z);
print(m)

