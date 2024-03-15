# A+B - 7, 2022년 1월 24일 21:35:44, 30864kb, 84ms, 105b
n=int(input())

for i in range(n):
  a,b=map(int,input().split())
  print("Case #{}: {}".format(i+1,a+b))
