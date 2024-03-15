# 공 넣기, 2023년 4월 11일 13:03:10, 2020kb, 0ms, 313b
#include <iostream>

int arr[100];

int main()
{
  int N,M,first,last, cnt, tmp;
  cnt = 0;
  std::cin>>N>>M;
  for(int i=0;i<M;i++) {
    std::cin>>first>>last>>tmp;
    for(int j=first-1;j<=last-1;j++)
      arr[j]=tmp;
  }
  for(int i=0;i<N;i++)
    std::cout<<arr[i]<<" ";
  std::cout<<"\n";
  
  return 0;
}

