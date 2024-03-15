# 통계학, 2023년 8월 11일 14:50:33, 55056kb, 472ms, 413b
# 통계학
# 최빈값을 어케 구하노?

import sys
import math
input = sys.stdin.readline

n=int(input())
d=dict()
l=list()
for i in range(n):
    x=int(input())
    l.append(x)
    if x in d:
        d[x]+=1
    else:
        d[x]=1
l.sort()
print(round(sum(l)/len(l)))
print(l[n//2])
m=max(d.values())
tmp = sorted(i for i in d.keys() if d[i]==m)
print(tmp[0] if len(tmp)==1 else tmp[1])
print(l[-1]-l[0])
