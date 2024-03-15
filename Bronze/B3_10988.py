# 팰린드롬인지 확인하기, 2022년 1월 26일 15:15:34, 30864kb, 68ms, 113b
a=input()
def pal(a):
  for i in range(len(a)//2):
    if(a[i]!=a[-i-1]):
      return 0
  return 1
print(pal(a))
