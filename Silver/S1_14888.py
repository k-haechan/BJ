# 연산자 끼워넣기, 2024년 2월 21일 19:53:40, 31120kb, 68ms, 801b
n = int(input())
numArr=list(map(int,input().split()))
opArr=list(map(int,input().split()))
m=float('inf')
M=-float('inf')

def dfs(depth,answer):
    global m
    global M

    if depth==n:
        if m>answer:
            m=answer
        if M<answer:
            M=answer
        return answer

    for i in range(4):
        if opArr[i]:
            tmp=answer
            if i==0:
                tmp+=numArr[depth]
            elif i==1:
                tmp-=numArr[depth]
            elif i==2:
                tmp*=numArr[depth]
            else:
                if tmp<0:
                    tmp=-(-tmp//numArr[depth])
                else:
                    tmp//=numArr[depth]
            opArr[i]-=1
            dfs(depth+1,tmp)
            opArr[i]+=1
dfs(1,numArr[0])
print(M)
print(m)
