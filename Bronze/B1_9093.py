# 단어 뒤집기, 2024년 3월 3일 00:45:44, 31120kb, 764ms, 96b
n=int(input())
for _ in range(n):
    s=input().split()
    s=[c[::-1] for c in s]
    print(*s)
