# 숫자의 개수, 2022년 1월 28일 23:12:40, 32320kb, 104ms, 144b
a=[int(input()) for _ in range(3)]
from functools import reduce
c=reduce(lambda x,y:x*y,a)
c=str(c)
for i in range(10):
  print(c.count(str(i)))
