# 곱셈, 2024년 2월 20일 13:25:56, 31120kb, 40ms, 179b
a,b,c=map(int,input().split())
a%=c
answer=1
b=format(b,'b')
for n in b:
    if n=='1':
        answer=(answer*answer*a)%c
    else:
        answer=(answer*answer)%c
print(answer)
