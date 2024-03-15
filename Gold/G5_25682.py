# 체스판 다시 칠하기 2, 2023년 8월 25일 19:32:30, 182936kb, 560ms, 1591b
import sys
input = sys.stdin.readline

n,m,k=map(int,input().split())
board=['0'*(m+1)]+['0'+input().rstrip() for _ in range(n)] # 예외처리를 안하기 위해 첫번째 행과 열을 0으로 패딩

check_Line_W=['0'+'WB'*(m//2)+'W'*(m%2)]
check_Line_B=['0'+'BW'*(m//2)+'B'*(m%2)]

check_W = ['0'*(m+1)]+(check_Line_W+check_Line_B)*(n//2)+check_Line_W*(n%2)
check_B = ['0'*(m+1)]+(check_Line_B+check_Line_W)*(n//2)+check_Line_B*(n%2)

prefix_sum_W=[[0]*(m+1) for _ in range(n+1)]
prefix_sum_B=[[0]*(m+1) for _ in range(n+1)]

# 누적합 구하기
for i in range(1,n+1):
    for j in range(1,m+1):
        prefix_sum_B[i][j]=int(check_B[i][j]!=board[i][j])+prefix_sum_B[i-1][j]+prefix_sum_B[i][j-1]-prefix_sum_B[i-1][j-1]
        prefix_sum_W[i][j]=int(check_W[i][j]!=board[i][j])+prefix_sum_W[i-1][j]+prefix_sum_W[i][j-1]-prefix_sum_W[i-1][j-1]

result=float('inf')

# 부분합 구하기
for i in range(1,n-k+2):
    for j in range(1,m-k+2):
        #prefix_sum[i][j]는 i,j까지의 합을 나타냄
        #prefix_sum[i][j]를 시작으로 하는 길이가 k인 정사각형의 누적합은 pSum[i-1+k]
        psb=prefix_sum_B[i-1+k][j-1+k]-prefix_sum_B[i-1][j-1+k]-prefix_sum_B[i-1+k][j-1]+prefix_sum_B[i-1][j-1] #k가 아닌 k-1인 이유 : 누적합에서 지점이 나타내는 것은 그 지점까지의 합.
        psw=prefix_sum_W[i-1+k][j-1+k]-prefix_sum_W[i-1][j-1+k]-prefix_sum_W[i-1+k][j-1]+prefix_sum_W[i-1][j-1] #누적합에서는 i번째 값을 구하기 위해서 i-1번째 값을 뺀다. i-1+k이므로 k-1이다.
        result=min(psb,psw,result)
print(result)
