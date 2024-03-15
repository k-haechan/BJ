# 파티가 끝나고 난 뒤, 2024년 3월 3일 17:47:11, 31120kb, 40ms, 102b
l,p=map(int,input().split())
people=l*p
A=list(map(int,input().split()))
print(*[a-people for a in A])
