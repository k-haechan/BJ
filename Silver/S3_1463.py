# 1로 만들기, 2024년 2월 18일 20:47:50, 31120kb, 40ms, 189b
import sys
input=sys.stdin.readline

d={1:0,2:1}
def f(n :int)->int:
    if n in d:
        return d[n]
    t = 1+min(n%3+f(n//3),n%2+f(n//2))
    d[n]=t
    return t
print(f(int(input())))
