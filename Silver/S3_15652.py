# N과 M (4), 2024년 2월 21일 11:42:18, 31120kb, 60ms, 221b
n,m=map(int,input().split())
answer=[]

def dfs(start):
    if len(answer)==m:
        print(*answer)
        return
    
    for i in range(start,n+1):
        answer.append(i)
        dfs(i)
        answer.pop()

dfs(1)
