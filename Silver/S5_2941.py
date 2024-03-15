# 크로아티아 알파벳, 2022년 2월 4일 11:08:15, 30864kb, 72ms, 130b
Croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
n=input()
for i in Croatia:
  if i in n:  
    n=n.replace(i,'*')
print(len(n))
