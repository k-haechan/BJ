# 평균, 2022년 1월 28일 23:35:29, 30840kb, 96ms, 84b
n=int(input())
a=list(map(int,input().split()))
mean=sum(a)/n
print(mean*100/max(a))
