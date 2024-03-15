# 킹, 퀸, 룩, 비숍, 나이트, 폰, 2023년 4월 11일 22:51:19, 2020kb, 0ms, 220b
#include <iostream>
#include <string>
int main()
{
  int k,q,l,b,kn,p;
  std::cin>>k>>q>>l>>b>>kn>>p;
  k=1-k;
  q=1-q;
  l=2-l;
  b=2-b;
  kn=2-kn;
  p=8-p;

  std::cout<<k<<" "<<q<<" "<<l<<" "<<b<<" "<<kn<<" "<<p;
  
}
