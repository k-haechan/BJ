# 부녀회장이 될테야, 2022년 2월 7일 00:44:51, 32972kb, 88ms, 116b
from math import comb
n = int(input())
for i in range(n):
    a=int(input());b=int(input())
    print(comb(a+b,a+1))
