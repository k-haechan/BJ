# 피보나치 수 5, 2022년 2월 11일 09:34:34, 30864kb, 68ms, 87b
def fibo(n):
  if n<=1: return n
  return fibo(n-1)+fibo(n-2)
print(fibo(int(input())))
