# 별 찍기 - 7, 2023년 4월 11일 23:11:25, 2020kb, 0ms, 377b
#include <iostream>

using namespace std;

int main()
{
  int n;
  std::cin>>n;

  for(int i=1;i<=n;i++) {
    for(int j=0;j<n-i;j++) std::cout<<" ";
    for(int k=0;k<2*i-1;k++) std::cout<<"*";
    std::cout<<'\n';
  }

  for(int i=n-1;i>=1;i--) {
    for(int j=0;j<n-i;j++) std::cout<<" ";
    for(int k=0;k<2*i-1;k++) std::cout<<"*";
    std::cout<<'\n';
  }  
  return 0;
}
