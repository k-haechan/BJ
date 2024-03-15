# 날짜 계산, 2024년 3월 2일 21:21:17, 31120kb, 40ms, 174b
e,s,m=map(int,input().split())
E=S=M=0
for year in range(15*28*19):
    if (E+year)%15+1== e and (S+year)%28+1== s and (M+year)%19+1 == m:
        print(year+1)
        break
