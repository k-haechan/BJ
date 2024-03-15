# 골드바흐의 추측, 2022년 2월 10일 21:56:10, 30860kb, 1004ms, 425b
MAX=10000
check=[0]*(MAX+1)
check[0]=check[1]=True  #True는 합성수
prime=[]
for i in range(2,MAX+1):
  if not check[i]:
    prime.append(i)
    j=i+i
    while j<=MAX:
      check[j]=True
      j+=i
prime=prime[1:]#2는 제외

for _ in range(int(input())):
  n=int(input())
  if n==4: print("2 2"); continue
  p1=-1
  for p in prime:
    if 2*p>n: break
    if not check[n-p]:
      p1=p
  print("{} {}".format(p1,n-p1))
