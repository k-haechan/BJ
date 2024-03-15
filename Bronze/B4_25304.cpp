# 영수증, 2023년 4월 11일 09:48:15, 2020kb, 0ms, 229b
#include <iostream>

int main()
{
  int X,N,a,b, sum;
  sum=0;
  std::cin >> X >> N;
  for(int i=0;i<N;i++) {
    std::cin >> a >> b;
    sum+=a*b;
  }
  if(X==sum) std::cout<<"Yes\n";
  else std::cout<<"No\n";
  
    return 0;
}
