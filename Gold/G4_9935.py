# 문자열 폭발, 2024년 3월 3일 01:12:59, 42300kb, 444ms, 202b
s=input()
bomb=list(input())
n=len(bomb)
stack=[]
for c in s:
    stack.append(c)
    if stack[-n:]==bomb:
        for _ in range(n):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')
