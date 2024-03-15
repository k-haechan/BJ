# ABCDE, 2023년 9월 5일 14:41:00, 31256kb, 896ms, 566b
# dfs의 시간복잡도 O(V+E)
# N = 2000, M=2000 -> O(4000), 노드의 개수 =2000 -> 800만 dfs 가능
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
A=[[] for _ in range(n)]

visited=[False]*n
for i in range(m):
    a,b=map(int,input().split())
    A[a].append(b)
    A[b].append(a)

def dfs(depth, x):
    if visited[x]:
        return
    visited[x]=True
    if depth==5:
        print(1)
        exit()
    for i in A[x]:
        dfs(depth+1,i)
    visited[x]=False
for i in range(n):
    dfs(1,i)
print(0)
