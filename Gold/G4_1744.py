# 수 묶기, 2023년 9월 7일 01:14:10, 31256kb, 40ms, 553b
import sys
input = sys.stdin.readline
n=int(input())
plus=[]
minus=[]
lp=0
lm=0
for _ in range(n):
    tmp=int(input())
    if tmp>0:
        plus.append(tmp)
        lp+=1
    else:
        minus.append(tmp)
        lm+=1

plus.sort(reverse=True)
minus.sort()

sum=0
for i in range(lp//2):
    if plus[2*i]!=1 and plus[2*i+1]!=1:
        sum+=(plus[2*i]*plus[2*i+1])
    else:
        sum+=(plus[2*i]+plus[2*i+1])

if lp%2==1:
    sum+=plus[-1]    

for i in range(lm//2):
    sum+=(minus[2*i]*minus[2*i+1])

if lm%2==1:
    sum+=minus[-1] 
print(sum)

