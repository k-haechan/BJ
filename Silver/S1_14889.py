# 스타트와 링크, 2024년 2월 21일 23:02:35, 31120kb, 1460ms, 739b
import sys
input=sys.stdin.readline

n=int(input())
stat_table=[list(map(int,input().split())) for _ in range(n)]
arr=[0]
m=float('inf')
def team_stat(team):
    total_stat=0
    n=len(team)
    for i in range(n):
        for j in range(i+1,n):
            person1,person2=team[i],team[j]
            total_stat+=stat_table[person1][person2]+stat_table[person2][person1]
    return total_stat

def dfs(depth=0):
    global m
    if depth==n//2-1:
        arr2=[x for x in range(n) if x not in arr]
        v=abs(team_stat(arr)-team_stat(arr2))
        if m>v:
            m=v
        return
    start_idx=arr[-1]+1# if arr else 0
    for i in range(start_idx,n):
        arr.append(i)
        dfs(depth+1)
        arr.pop()

dfs()
print(m)
