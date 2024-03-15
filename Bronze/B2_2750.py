# 수 정렬하기, 2022년 2월 25일 23:53:14, 30864kb, 104ms, 101b
a=[]
for _ in range(int(input())):
  a+=[int(input())]
a.sort()
for i in range(len(a)):
  print(a[i])
