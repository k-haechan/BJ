# 과자, 2022년 1월 26일 12:22:51, 30864kb, 68ms, 89b
a=list(map(int,input().split()))
answer=a[0]*a[1]-a[2]
print(answer if(answer>=0) else 0)
