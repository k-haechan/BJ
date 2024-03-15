# 수들의 합, 2022년 1월 25일 11:44:01, 30864kb, 124ms, 80b
S=int(input())
a=1
while(True):
  if((a**2+a)>2*S):
    break;
  a+=1
print(a-1)
