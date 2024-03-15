# 주사위 세개, 2022년 1월 26일 12:12:09, 34484kb, 64ms, 266b
a=list(map(int,input().split()))
from collections import Counter
cnt=Counter(a)

if (cnt.most_common(1)[0][1]==3):
  print(10000+cnt.most_common(1)[0][0]*1000)
elif (cnt.most_common(1)[0][1]==2):
  print(1000+cnt.most_common(1)[0][0]*100)
else:
  print(max(cnt)*100)
