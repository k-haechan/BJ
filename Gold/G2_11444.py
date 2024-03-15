# 피보나치 수 6, 2024년 2월 20일 15:53:50, 31120kb, 48ms, 549b
n=int(input())

def mat_mul(mat1,mat2):
    mat=[[0]*len(mat2[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                mat[i][j]+=mat1[i][k]*mat2[k][j]
            mat[i][j]%=1000000007
    return mat

def fibo(n):
    fibo_mat=[[1,1],[1,0]]
    mat=[[1,0],[0,1]]
    b=format(n,'b')
    for b_ in b:
        mat=mat_mul(mat,mat)
        if b_=='1':
            mat=mat_mul(mat,fibo_mat)
    mat=mat_mul(mat,[[1],[0]])
    print(mat[1][0])

fibo(n)
