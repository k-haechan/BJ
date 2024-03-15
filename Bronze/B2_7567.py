# 그릇, 2022년 1월 26일 14:31:54, 30864kb, 72ms, 101b
a=list(input())
n=10
for i in range(len(a)-1):
  if a[i]!=a[i+1]:
    n+=10
  else:
    n+=5
print(n)
