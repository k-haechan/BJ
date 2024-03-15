# ACM 호텔, 2022년 2월 5일 16:49:37, 30864kb, 76ms, 118b
for _ in range(int(input())):
  H,W,N=map(int,input().split())
  b=N//H+1
  c=N%H
  if c==0: c=H;b-=1
  print(c*100+b)
