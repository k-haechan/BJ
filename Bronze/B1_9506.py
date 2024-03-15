# 약수들의 합, 2022년 1월 27일 01:32:19, 30860kb, 68ms, 410b
while(True):
  n=int(input())
  if(n==-1):
    break;
  divisorsList=[]
  for i in range(2,int((n**(1/2))+1)):
    if(n%i==0):
      divisorsList.extend([i,int(n/i)])
    
  if (int(sum(divisorsList))+1)==n:
    divisorsList.append(1)
    divisorsList.sort()
    divisorsList=list(map(str,divisorsList))
    print("{} =".format(n)," + ".join(divisorsList)) 
  
  else:
    print("{} is NOT perfect.".format(n))
