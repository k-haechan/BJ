# 소수 구하기, 2022년 2월 9일 13:41:38, 38532kb, 392ms, 243b
m,n=map(int,input().split())
prime=[True]*(n+1)
prime[0],prime[1]=0,0

for i in range(n+1):
  if not prime[i]: continue
  if i*i>n: break
  for j in range(2*i,n+1,i):
    prime[j]=False

for i in range(m,n+1):
  if prime[i]==True:
    print(i)
