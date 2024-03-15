# 두 수의 합, 2024년 2월 28일 13:13:08, 41844kb, 452ms, 282b
n=int(input())
A=sorted(map(int,input().split()))
x=int(input())
answer=0
for i in range(n):
    y=x-A[i]
    s,e=i+1,n-1
    while s<=e:
        m=(s+e)//2
        if A[m]<y:
            s=m+1
        else:
            e=m-1
    if s!=n and A[s]==y:
        answer+=1
print(answer)
