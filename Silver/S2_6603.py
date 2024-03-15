# 로또, 2024년 2월 27일 20:25:53, 31120kb, 44ms, 307b
def dfs(n,r,start=0,ans=[]):
    if len(ans)==r:
        print(*ans)
    for i in range(start,n):
        ans.append(arr[i])
        dfs(n,r,i+1,ans)
        ans.pop()

while True:
    A=list(map(int,input().split()))
    if len(A)==1 and A[0]==0:
        break
    n,arr=A[0],A[1:]
    dfs(n,6)
    print()
