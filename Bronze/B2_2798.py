# 블랙잭, 2022년 2월 15일 10:56:04, 30860kb, 104ms, 257b
n,m=map(int,input().split())
a=list(map(int,input().split()))
#n개의 카드중 3개를 고르고 합이 m인
tmp=0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if tmp<a[i]+a[j]+a[k]<=m:
        tmp=a[i]+a[j]+a[k]
print(tmp)
