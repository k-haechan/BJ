# 알람 시계, 2021년 11월 13일 14:13:43, 29200kb, 68ms, 211b
h,m=input().split()
h=int(h);  m=int(m)
if(m not in range(60) or h not in range(24)):
    print("Out of range!")

if(m>=45):
    m-=45
else:
    m+=15
    if(h==0):
        h=23
    else:
        h-=1
print(h,m)
