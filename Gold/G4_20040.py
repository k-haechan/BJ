# 사이클 게임, 2024년 2월 24일 13:10:31, 77680kb, 776ms, 466b
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

n,m=map(int,input().split())
parent=list(range(n))

def find(a):
    if parent[a]!=a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a
        return False
    else:
        return True
answer=0
for i in range(m):
    a,b=map(int,input().split())
    if union(a,b):
        answer=i+1
        break
print(answer)
