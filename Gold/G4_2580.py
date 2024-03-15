# 스도쿠, 2023년 8월 18일 09:14:15, 138680kb, 2572ms, 1017b
# 스도쿠
# 넘파이를 이용한 풀이도 한번 해보기
arr=[list(map(int,input().split())) for _ in range(9)] # 입력값을 배열로 받기
def check(n,r,c):
    for i in range(9):
        if arr[r][i]==n or arr[i][c]==n: # 같은 열 또는 같은 행에 존재하는지 확인
            return False
    for i in range(3*(r//3),3*(r//3)+3): # 사각형 안에 존재하는지 확인
        for j in range(3*(c//3),3*(c//3)+3):
            if n==arr[i][j]:
                return False
    return True                          # 모두 존재하지 않으면 True 반환 
def sudoku():
    for i in range(9): #0~8
        for j in range(9):
            if arr[i][j]==0: # 만약에 안채워진 곳이 있다면
                for k in range(1,10):
                    if check(k,i,j):
                        arr[i][j]=k
                        sudoku()
                        arr[i][j]=0
                return
                
    for a in arr:
        print(*a)
    exit(0)            

sudoku()

