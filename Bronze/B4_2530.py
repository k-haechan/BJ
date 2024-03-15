# 인공지능 시계, 2022년 1월 24일 22:18:36, 30864kb, 76ms, 146b
A,B,C=map(int,input().split())
t=int(input())
C+=t

if(C>59):
  B+=(C//60)
  C%=60

if(B>59):
  A+=(B//60)
  B%=60

if(A>23):
  A%=24
print(A,B,C)
