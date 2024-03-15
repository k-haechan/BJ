# 그룹 단어 체커, 2022년 2월 4일 12:56:46, 31256kb, 48ms, 269b
cnt=0
for _ in range(int(input())):
   a=input()
   if len(a) == 1:
     cnt+=1
   else: 
    tmp=[a[0]]
    for i in range(len(a)-1):
      if a[i]!=a[i+1]:
        if a[i+1] in tmp:
          break
        tmp+=[a[i+1]]
      if i==len(a)-2:
        cnt+=1
print(cnt)
