# 주사위 게임, 2022년 1월 27일 01:52:14, 30860kb, 68ms, 165b
score=[100,100]
for _ in range(int(input())):
  a,b=map(int,input().split())
  if(a>b):
    score[1]-=a
  elif(b>a):
    score[0]-=b

print(score[0])
print(score[1])
