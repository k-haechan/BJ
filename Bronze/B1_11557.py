# Yangjojang of The Year, 2022년 1월 27일 13:47:29, 30860kb, 68ms, 163b
for _ in range(int(input())):
  a=[0,0]
  for _ in range(int(input())):
    tmp=input().split();tmp[1]=int(tmp[1]);
    if(tmp[1]>=a[1]):
      a=tmp
  print(a[0])
