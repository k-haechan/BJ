# 접미사 배열, 2024년 3월 3일 00:48:59, 31120kb, 44ms, 108b
s=input()
answer=[]
for i in range(len(s)):
    answer.append(s[i:])
for s_ in sorted(answer):
    print(s_)
