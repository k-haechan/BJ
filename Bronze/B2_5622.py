# 다이얼, 2022년 2월 3일 09:07:05, 30864kb, 72ms, 236b
a=input()
t=0
for i in a:
  b=ord(i)-65
  if b < 3:
    t+=3
  elif b < 6:
    t+=4
  elif b < 9:
    t+=5
  elif b < 12:
    t+=6
  elif b < 15:
    t+=7
  elif b < 19:
    t+=8
  elif b < 22:
    t+=9
  elif b < 26:
    t+=10
print(t)
