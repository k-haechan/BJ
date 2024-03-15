# N과 M (1), 2024년 2월 20일 23:07:49, 31120kb, 176ms, 311b
n,m=map(int,input().split())

visited=[False]*(n+1)
arr=[]

def combi():
    if len(arr)==m:
        print(*arr)
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i]=True
        arr.append(i)
        combi()
        visited[i]=False
        arr.pop()
combi()
