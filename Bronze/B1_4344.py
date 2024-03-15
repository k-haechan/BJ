# 평균은 넘겠지, 2022년 1월 29일 00:11:36, 31256kb, 48ms, 188b
for _ in range(int(input())):
  a=list(map(int,input().split()))
  mean=(sum(a)-a[0])/a[0]
  b=0
  for i in range(a[0]):
    if a[i+1]>mean:
      b+=1
  z=b/a[0]*100
  print(f'{z:.3f}%')

