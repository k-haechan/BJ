# N과 M (2), 2024년 2월 21일 11:23:59, 31120kb, 40ms, 257b
n,m=map(int,input().split())
answer=[]

def dfs(start):
    if len(answer)==m:
        print(*answer)
        return
    for i in range(start,n+1):
        if i not in answer:
            answer.append(i)
            dfs(i+1)
            answer.pop()
dfs(1)
