# 베르트랑 공준, 2022년 2월 9일 14:20:58, 32788kb, 608ms, 305b
n=123456*2
prime=[True]*(n+1)
prime[0],prime[1]=0,0

for i in range(n+1):
  if not prime[i]: continue
  if i*i>n: break
  for j in range(2*i,n+1,i):
    prime[j]=False

while n:
    n=int(input())
    if n==0: break
    cnt=0
    for i in range(n+1,2*n+1):
      if prime[i]:
        cnt+=1
    print(cnt)
