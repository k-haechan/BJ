# 단어 공부, 2022년 2월 2일 00:38:59, 33212kb, 200ms, 203b
s=input().upper()
a={}

for i in s:
 if i not in a:
   a[i]=1
 else:
   a[i]+=1

c=sorted(a.items(),key=lambda x:x[1],reverse=True)

if len(c)!=1 and c[0][1]==c[1][1]:
  print('?')
else:
  print(c[0][0])
