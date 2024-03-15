# 사분면, 2022년 1월 27일 20:31:28, 30860kb, 108ms, 320b
Q1,Q2,Q3,Q4,AXIS =0,0,0,0,0

for _ in range(int(input())):
  a,b=map(int,input().split())
  if(a>0 and b>0):
    Q1+=1
  elif(a<0 and b>0):
    Q2+=1
  elif(a<0 and b<0):
    Q3+=1
  elif(a>0 and b<0):
    Q4+=1
  else:
    AXIS+=1

print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("Q4:",Q4)
print("AXIS:",AXIS)    
