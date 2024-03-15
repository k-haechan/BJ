# 문자열 반복, 2022년 2월 1일 23:14:04, 30860kb, 68ms, 108b
for _ in range(int(input())):
  a,b=input().split()
  a=int(a)
  for i in b:
    print(i*a,end='')
  print()
