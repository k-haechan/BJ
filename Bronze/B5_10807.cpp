# 개수 세기, 2023년 4월 11일 12:01:56, 2020kb, 0ms, 239b
#include <iostream>

int arr[100];

int main()
{
  int N,v,cnt;
  cnt = 0;
  std::cin>>N;
  for(int i=0;i<N;i++)
    std::cin>>arr[i];
  
  std::cin>>v;
  for(int i=0;i<N;i++)
    if(arr[i]==v)
      cnt++;
  std::cout<<cnt;
  return 0;
}

