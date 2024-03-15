# 카드 역배치, 2024년 2월 28일 12:25:50, 31120kb, 44ms, 171b
CARD=list(range(21))
for _ in range(10):
    a,b=map(int,input().split())
    while a<b:
        CARD[a],CARD[b]=CARD[b],CARD[a]
        a+=1
        b-=1
print(*CARD[1:])
