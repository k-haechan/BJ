# A와 B, 2023년 11월 29일 19:30:39, 31252kb, 40ms, 210b
import sys
input = sys.stdin.readline

S=list(input().rstrip())
T=list(input().rstrip())

while len(S)!=len(T):
    if T[-1]=='A':
        T.pop()
    else:
        T.pop()
        T.reverse()

print(int(S==T))
