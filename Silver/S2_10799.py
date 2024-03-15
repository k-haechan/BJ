# 쇠막대기, 2024년 2월 29일 19:43:49, 31552kb, 64ms, 198b
answer=0
A=[]
s=input()
for i in range(len(s)):
    if s[i]=='(':
        A.append('(')
        answer+=1
    else:
        A.pop()
        if s[i-1]=='(':
            answer+=len(A)-1
print(answer)
