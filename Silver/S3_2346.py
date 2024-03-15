# 풍선 터뜨리기, 2023년 8월 15일 15:47:50, 34104kb, 60ms, 314b
# 풍선 터뜨리기
from collections import deque

n=int(input())
dq=deque(enumerate(map(int,input().split()),1))
answer=[]
for _ in range(n):
    tmp = dq.popleft()
    answer.append(tmp[0])
    if tmp[1]>0:
        dq.rotate(-tmp[1]+1)
    else:
        dq.rotate(-tmp[1])
    
print(' '.join(map(str,answer)))
