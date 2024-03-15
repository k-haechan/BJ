# 행렬 제곱, 2024년 2월 20일 14:15:33, 31120kb, 40ms, 583b
n,b=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]

def mat_mul(mat1,mat2,n):
    mat=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat[i][j]=(mat[i][j]+mat1[i][k]*mat2[k][j])%1000
    return mat

answer=[[0 if i!=j else 1 for j in range(n)] for i in range(n)]
b=format(b,'b')
for b_ in b:
    if b_=='1':
        answer=mat_mul(answer,answer,n)
        answer=mat_mul(answer,matrix,n)
    else:
        answer=mat_mul(answer,answer,n)
for ans in answer:
    print(*ans)
