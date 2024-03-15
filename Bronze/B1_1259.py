# 팰린드롬수, 2024년 3월 2일 23:16:13, 31120kb, 44ms, 95b
while True:
    s=input()
    if s=='0':
        break
    print('yes' if s==s[::-1] else 'no')
