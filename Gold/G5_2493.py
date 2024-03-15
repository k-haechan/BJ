# 탑, 2024년 3월 1일 17:04:33, 114664kb, 632ms, 230b
n=int(input())
A=list(map(int,input().split()))
answer=[0]*n
stack=[(0,float('inf'))]
for i in range(len(A)):
    while stack[-1][1]<=A[i]:
        stack.pop()
    answer[i]=stack[-1][0]
    stack.append((i+1,A[i]))
print(*answer)
