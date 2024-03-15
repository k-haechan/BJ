# N-Queen, 2023년 8월 11일 22:01:36, 31256kb, 23688ms, 1016b
n = int( input() )
# n : 1 ~ 15
isColumnUsed = [ False for i in range(n) ]
# 우하향 대각선 x-y 가 -n+1 ~ n-1
# index 는 2n-1개가 필요.
# x-y 가 -n+1 인 경우 (n-1)을 더해 isDownRightUsed[0]을 참조
isDownRightUsed = [ False for i in range(2*n-1) ]
isUpRightUsed = [ False for i in range(2*n-1) ]
count = 0

def backtracking( depth ):

  if( depth == n ):
    global count
    count += 1  
    return 

  # depth 번째 row에 대해서 col0 ~ col(n-1)까지 조사
  for i in range(n):
    if( isColumnUsed[i] or isDownRightUsed[depth-i+n-1] or isUpRightUsed[depth + i] ):
      # ( depth, i )에 둘수 없다
      continue
    
    # ( depth, i )에 둔 경우
    isColumnUsed[i] = True
    isDownRightUsed[ depth-i+n-1 ] = True
    isUpRightUsed[ depth + i ] = True
    
    # 다음 row (depth + 1 진행)
    backtracking( depth+1 )

    # 무르기
    isColumnUsed[i] = False
    isDownRightUsed[ depth-i+n-1 ] = False
    isUpRightUsed[ depth + i ] = False

backtracking(0)
print(count)
