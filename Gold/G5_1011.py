# Fly me to the Alpha Centauri, 2022년 2월 10일 11:26:37, 33376kb, 52ms, 208b
import math
for _ in range(int(input())):
  x,y=map(int,input().split())
  d=y-x
  z=int(math.sqrt(d))
  if z**2==d:
    n=z*2-1#n번째값 
  else:
    if d<=z*(z+1):
      n=z*2
    else: n=z*2+1
  print(n)
