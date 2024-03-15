# 동전 0, 2024년 2월 20일 18:48:00, 31120kb, 44ms, 171b
n,k = map(int,input().split())
answer=0
A=[int(input()) for _ in range(n)]
for i in range(n-1,-1,-1):
    if k>=A[i]:
        answer+=k//A[i]
        k%=A[i]
print(answer)
