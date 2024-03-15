# 공 바꾸기, 2023년 4월 11일 16:13:14, 2020kb, 0ms, 349b
#include <iostream>

int arr[101];

int main()
{
  int N, M, cnt, tmp, a,b;
  cnt = 0;
  std::cin>>N>>M;
  for(int i=1;i<N+1;i++)
    arr[i]=i;

  for(int i=0;i<M;i++) {
    std::cin>>a>>b;
    tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
  }
  
  
  
  for(int i=1;i<N+1;i++)
    std::cout<<arr[i]<<" ";
  std::cout<<"\n";
  
  return 0;
}

