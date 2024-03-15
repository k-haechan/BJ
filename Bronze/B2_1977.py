# 완전제곱수, 2024년 3월 3일 16:45:38, 31120kb, 52ms, 199b
m,n=int(input()),int(input())
m_,n_=int(m**(0.5)),int(n**(0.5))
if m_**2!=m:
    m_+=1
answer=[x**2 for x in range(m_,n_+1)]
if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)
