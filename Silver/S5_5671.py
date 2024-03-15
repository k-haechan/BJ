# 호텔 방 번호, 2022년 1월 28일 12:01:34, 30860kb, 740ms, 181b
while True:
  try:
    n,m=map(int,input().split())
    cnt=0
    for i in range(n,m+1):
      if(len(set(str(i)))==len(str(i))):
        cnt+=1
    print(cnt)
  except:
    break;

