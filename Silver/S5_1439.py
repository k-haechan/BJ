# 뒤집기, 2024년 3월 3일 00:08:05, 31120kb, 40ms, 139b
answer=[0]*2
s=input()
idx=0
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        answer[idx]+=1
        idx=(idx+1)%2
print(max(answer))
