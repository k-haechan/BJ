# 지능형 기차, 2024년 3월 3일 16:07:11, 31120kb, 40ms, 134b
answer=0
tmp=0
for _ in range(4):
    a,b=map(int,input().split())
    tmp=tmp+b-a
    if answer<tmp:
        answer=tmp
print(answer)
