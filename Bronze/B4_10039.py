# 평균 점수, 2022년 1월 25일 21:10:06, 30860kb, 68ms, 118b
stdnt=[]
for i in range(5):
  stdnt.append(int(input()))
  if(stdnt[i]<40):
    stdnt[i]=40
print(int(sum(stdnt)/5))


