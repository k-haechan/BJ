# 사분면 고르기, 2021년 11월 13일 13:59:17, 29200kb, 76ms, 170b
x=input(); y=input()
x=int(x);  y=int(y)

if(x>0):
    if(y>0):
        print(1)
    else:
        print(4)
else:
    if(y>0):
        print(2)
    else:
        print(3)
