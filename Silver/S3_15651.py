# N과 M (3), 2024년 2월 21일 11:30:40, 31120kb, 1944ms, 190b
n,m=map(int,input().split())
arr=[]

def dfs():
    if len(arr)==m:
        print(*arr)
        return
    for i in range(1,n+1):
        arr.append(i)
        dfs()
        arr.pop()

dfs()
