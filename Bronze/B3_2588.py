# 곱셈, 2022년 1월 24일 19:29:40, 30860kb, 72ms, 95b
a=int(input())
b=input()
for i in reversed(range(len(b))):
  print(a*int(b[i]))
print(a*int(b))
