# 분수찾기, 2022년 2월 5일 01:52:02, 30864kb, 72ms, 148b
n=int(input())
i=0;
while n>i*(i+1)/2:
  i+=1
k=int(n-i*(i-1)/2)
if i%2==1:
  print("{}/{}".format(i-k+1,k))
else:
  print("{}/{}".format(k,i-k+1))

