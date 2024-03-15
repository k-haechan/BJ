# OX퀴즈, 2022년 1월 26일 16:30:54, 30864kb, 80ms, 167b
for _ in range(int(input())):
  A=input()
  B=A.split(sep='X')
  B=list(filter(None,B))
  Sum=0
  for i in range(len(B)):
    Sum+=sum(range(len(B[i])+1))
  print(Sum)
