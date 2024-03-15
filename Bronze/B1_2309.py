# 일곱 난쟁이, 2024년 2월 28일 11:51:52, 31120kb, 40ms, 186b
from itertools import combinations
A=[int(input()) for _ in range(9)]
for B in list(combinations(A,7)):
    if sum(B)==100:
        for b in sorted(B):
            print(b)
        break
