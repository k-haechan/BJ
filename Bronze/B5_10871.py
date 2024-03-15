# X보다 작은 수, 2022년 1월 28일 22:25:49, 30864kb, 76ms, 117b
N,X=map(int,input().split())
a=list(map(int,input().split()))
for i in range(N):
  if a[i]<X:
    print(a[i],end=' ')
