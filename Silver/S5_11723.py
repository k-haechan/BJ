# 집합, 2024년 3월 3일 15:05:19, 31120kb, 4124ms, 528b
import sys
input=sys.stdin.readline

T=int(input())
S=set()

for _ in range(T):
    s=input().rstrip().split()
    cal=s[0]
    x=0
    if len(s)>1:
        x=int(s[1])
        
    if cal=='add':
        S.add(x)
    elif cal=='remove':
        if x in S:
            S.remove(x)
    elif cal=='check':
        print(1 if x in S else 0)
    elif cal=='toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif cal=='all':
        S=set(range(1,21))
    elif cal=='empty':
        S.clear()
