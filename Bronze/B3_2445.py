# 별 찍기 - 8, 2024년 2월 28일 12:35:55, 31120kb, 40ms, 137b
n=int(input())
for i in range(1,n+1):
    print('*'*i+' '*(2*(n-i))+'*'*i)
for i in range(n-1,0,-1):
    print('*'*i+' '*(2*(n-i))+'*'*i)
