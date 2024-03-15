# 핸드폰 요금, 2024년 2월 28일 12:22:11, 31120kb, 40ms, 294b
n=int(input())
A=list(map(int,input().split()))

def y_bill(time):
    return (time//30+1)*10

def m_bill(time):
    return (time//60+1)*15

y=sum(list(map(y_bill,A)))
m=sum(list(map(m_bill,A)))
if m<y:
    answer=['M',m]
elif m>y:
    answer=['Y',y]
else:
    answer=['Y','M',m]
print(*answer)
