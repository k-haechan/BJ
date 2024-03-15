# 명령 프롬프트, 2024년 3월 2일 23:47:56, 31120kb, 44ms, 140b
n=int(input())
s=input()
for _ in range(n-1):
    tmp=input()
    s=''.join([s[i] if s[i]==tmp[i] else '?' for i in range(len(s))])
print(s)
