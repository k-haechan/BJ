# 셀프 넘버, 2022년 1월 29일 22:38:20, 30860kb, 616ms, 175b
a=list(range(1,10000))
c=[]
for i in range(1,10000):
  b=i+sum(map(int,list(str(i))))
  if (b not in c and b<10000):
    a.remove(b)
    c.append(b)
print(*sorted(a),sep='\n')
