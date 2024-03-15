# 칵테일, 2023년 9월 12일 09:25:56, 31388kb, 44ms, 712b
N=int(input())
A=[[] for _ in range(N)]
visited = [False] * N
D=[0]*N
lcm=1

def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
    
def DFS(v):
    visited[v]=True
    for i in A[v]: # 나랑 연결되어 있는 것들 중
        next=i[0]
        if not visited[next]: # 아직 처리하지 않았다면
            D[next]=D[v]*i[2]//i[1]
            DFS(next)

for i in range(N-1):
    a,b,p,q = map(int, input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))
    lcm *= (p*q//gcd(p,q)) # 각 라운드에서 pq의 lcm을 곱한다. 
D[0] = lcm
DFS(0)
mgcd = D[0]

for i in range(1,N):
    mgcd = gcd(mgcd,D[i])

for i in range(N):
    print(int(D[i]//mgcd),end=' ')
