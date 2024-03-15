# 바구니 순서 바꾸기, 2023년 4월 11일 23:44:41, 2020kb, 0ms, 361b
#include <iostream>
#include <algorithm>

using namespace std;

int arr[101];

int main()
{
  int n,m, start, middle, end;
  cin>>n>>m;
  for(int i=1;i<=n;i++)
    arr[i]=i;

  for(int i=0;i<m;i++) {
    cin>>start>>end>>middle;
    rotate(arr+start,arr+middle, arr+end+1);     
  }
  for(int i=1;i<=n;i++)
      cout<<arr[i]<<' ';
    cout<<'\n';
  return 0;
}
