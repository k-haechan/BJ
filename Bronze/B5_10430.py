# 나머지, 2022년 1월 24일 18:50:13, 30864kb, 80ms, 99b
A,B,C=map(int,input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')

