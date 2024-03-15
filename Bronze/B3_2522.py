# 별 찍기 - 12, 2024년 3월 3일 16:11:15, 31120kb, 40ms, 118b
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)

for i in range(n-1,0,-1):
    print(' '*(n-i)+'*'*i)
