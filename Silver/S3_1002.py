# 터렛, 2022년 2월 9일 23:21:53, 31256kb, 56ms, 315b
for _ in range(int(input())):
  a=list(map(int,input().split()))
  r1,r2=a[2],a[5]
  d=(a[3]-a[0])**2+(a[4]-a[1])**2
  
  if (a[0],a[1],a[2])==(a[3],a[4],a[5]):
    print(-1)
  else:
    if d==(r1+r2)**2 or d==(r1-r2)**2:
      print(1)
    elif d>(r1+r2)**2 or d<(r1-r2)**2:
      print(0)
    else:
      print(2)
