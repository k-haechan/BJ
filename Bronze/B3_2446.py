# 별 찍기 - 9, 2024년 2월 28일 12:42:05, 31120kb, 40ms, 126b
n=int(input())
for i in range(n):
    print(' '*i+'*'*(2*(n-i)-1))
for i in range(n-2,-1,-1):
    print(' '*i+'*'*(2*(n-i)-1))
