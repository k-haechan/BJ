# 팩토리얼, 2022년 2월 11일 09:33:00, 30860kb, 68ms, 82b
def facto(n):
  if n<=1: return 1
  return n*facto(n-1)
print(facto(int(input())))
