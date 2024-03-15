# 센서, 2024년 3월 1일 21:43:29, 32656kb, 48ms, 157b
n=int(input())
k=int(input())
A=sorted(set(map(int,input().split())))
B=sorted(A[i]-A[i-1] for i in range(1,len(A)))
print(sum(B[:-k+1]) if k!=1 else sum(B))
