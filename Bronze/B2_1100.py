# 하얀 칸, 2024년 3월 2일 23:51:47, 31120kb, 40ms, 164b
board=[input() for _ in range(8)]
answer=0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0 and board[i][j]=='F':
            answer+=1
print(answer)
