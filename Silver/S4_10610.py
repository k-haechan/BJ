# 30, 2024년 3월 2일 23:58:20, 32912kb, 64ms, 173b
s=input()
if sum(map(int,list(s)))%3==0 and '0' in s:
    tmp=sorted([c for c in s if c!='0'],reverse=True)
    print(''.join(tmp)+(len(s)-len(tmp))*'0')
else:
    print(-1)
