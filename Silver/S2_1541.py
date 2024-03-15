# 잃어버린 괄호, 2024년 2월 20일 19:34:11, 31120kb, 40ms, 182b
a=input().split('-')
answer=0
for i in range(len(a)):
    if i==0:
        answer+=sum(map(int,a[i].split('+')))
    else:
        answer-=sum(map(int,a[i].split('+')))
print(answer)
