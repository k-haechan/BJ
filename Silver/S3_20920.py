# 영단어 암기는 괴로워, 2023년 8월 11일 14:39:14, 59880kb, 332ms, 328b
# 영단어 암기는 괴로워
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
d={}
for _ in range(n):
    x=input().rstrip('\n')
    if len(x)>=m:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
d=sorted(d.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for x in d:
    print(x[0])
