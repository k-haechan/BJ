# 오민식의 고민, 2023년 9월 19일 18:52:08, 31256kb, 44ms, 843b
# 오민식의 고민
import sys
input = sys.stdin.readline

n,sCity,eCity,m = map(int,input().split())
edges=[]
for _ in range(m):
    s,e,w=map(int,input().split())
    edges.append((s,e,w))
price=list(map(int,input().split()))
distance=[-sys.maxsize]*n
distance[sCity]=price[sCity]

for i in range(n+n): # 충분한 사이클 검증을 위해 N번 더 실행한다.
    for s,e,w in edges:
        if distance[s]==-sys.maxsize:
            continue
        elif distance[s] == sys.maxsize:
            distance[e]=sys.maxsize
        elif distance[e]<distance[s]+price[e]-w:
            distance[e]=distance[s]+price[e]-w
            if i>=n-1:
                distance[e]=sys.maxsize

if distance[eCity]==sys.maxsize:
    print('Gee')
elif distance[eCity]==-sys.maxsize:
    print('gg')
else:                    
    print(distance[eCity])
