# A+B - 8, 2021년 11월 16일 09:24:03, 29200kb, 68ms, 155b
import sys

N=int(sys.stdin.readline())
for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    print("Case #{}:".format(i+1),a,"+",b,"=",a+b)
