# 과제 안 내신 분..?, 2023년 4월 11일 16:18:09, 2020kb, 0ms, 217b
#include <iostream>

bool arr[31] = {0,};
int main()
{
  int n;
  for(int i=0;i<28;i++) {
    std::cin>>n;
    arr[n] = true;
  }
  for(int i=1;i<31;i++)
    if(arr[i]==0)
      std::cout<<i<<'\n';
    
  return 0;
}

