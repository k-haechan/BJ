# 최소 스패닝 트리, 2023년 9월 26일 16:40:10, 47788kb, 300ms, 531b
import sys
input = sys.stdin.readline

v,e=map(int,input().split())
edges=[]
for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
edges.sort()

parent=list(range(v+1))
def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
    
def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return False
    elif a>b:
        a,b=b,a
    parent[b]=a
    return True

mst=0
for w,a,b in edges:
    if union(a,b):
        mst+=w
print(mst)
