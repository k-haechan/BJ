# 부분수열의 합, 2024년 3월 2일 19:50:46, 31120kb, 348ms, 218b
from itertools import combinations
n,s=map(int,input().split())
A=list(map(int,input().split()))
answer=0
for i in range(1,n+1):
    for x in combinations(A,i):
        if sum(x)==s:
            answer+=1
print(answer)
