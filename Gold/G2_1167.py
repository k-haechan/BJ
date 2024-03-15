# 트리의 지름, 2023년 9월 5일 20:25:21, 71704kb, 568ms, 1071b
# 트리의 지름 구하기
# 트리의 최대 길이 구하기. 
# 트리의 지름은 아무거나 골라서 최대길이 구한 후 그 노드에서 다시 최대길이를 구한 것이다.
# 문제 풀이 방법 : 최대 길이 구하기는 dfs로 구할 수 있다.
import sys
from collections import deque
input = sys.stdin.readline

v=int(input())
A=[[]for _ in range(v+1)]

# 가중치 인접 리스트(A) 구하기
for _ in range(v):
    tmp = list(map(int,input().rstrip().split()))
    ptr=1
    while tmp[ptr]!=-1:
        A[tmp[0]].append((tmp[ptr],tmp[ptr+1]))
        ptr+=2

def dfs(node):
    global v
    dq=deque()
    dq.append(node)
    width=[0]*(v+1)
    visited=[False]*(v+1)

    visited[node]=True
    _max=[0,0]

    while dq:
        x=dq.popleft()
        for i,w in A[x]:
            if not visited[i]:
                visited[i]=True
                dq.append(i)
                width[i]=width[x]+w
                if _max[0]<width[i]:
                    _max=width[i],i
    return _max

_max = dfs(1)
__max = dfs(_max[1])
print(__max[0])
