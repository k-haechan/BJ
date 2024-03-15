# 별 찍기 - 6, 2024년 2월 28일 12:33:20, 31120kb, 40ms, 71b
n=int(input())
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))
