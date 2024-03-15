# 연결 요소의 개수, 2023년 9월 5일 02:55:41, 65156kb, 1304ms, 465b
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int,input().split())
A=[[] for _ in range(n+1)]
visited=[False]*(n+1)
cnt=0

for _ in range(m):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

def dfs(v):
    if not visited[v]: # 방문하지 않았으면,
        visited[v]=True
        for i in A[v]:
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)
