# 바구니 뒤집기, 2023년 4월 11일 16:28:21, 2020kb, 0ms, 388b
#include <iostream>
using namespace std;

int arr[101] = {0,};
int main()
{
  int N,M,a,b,d, tmp;
  cin>>N>>M;
  for(int i=1;i<N+1;i++)
    arr[i]=i;
  
  for(int i=0;i<M;i++){
    cin>>a>>b;
    d = (b-a+1)/2;
    for(int j=0;j<d;j++) {
      tmp=arr[a+j];
      arr[a+j]=arr[b-j];
      arr[b-j]=tmp;
    }
  }
  for(int i=1;i<N+1;i++)
    cout<<arr[i]<<" ";
  cout<<"\n";
  return 0;
}
