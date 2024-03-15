# 오븐 시계, 2022년 1월 24일 22:00:47, 31252kb, 52ms, 108b
h,m=map(int,input().split())
t=int(input())
m+=t
if(m>59):
  h+=(m//60)
  m%=60
if(h>23):
  h%=24
print(h,m)
