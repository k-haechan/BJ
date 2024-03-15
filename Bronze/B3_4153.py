# 직각삼각형, 2022년 2월 9일 21:50:22, 30860kb, 72ms, 209b
while True:
  rt=list(map(int,input().split()))
  if rt == [0,0,0]:
    break;

  hypotenuse=max(rt)
  rt.remove(hypotenuse)
  if rt[0]**2 + rt[1]**2 == hypotenuse**2:
    print('right')
  else: print('wrong')
