# 문자열, 2023년 4월 11일 21:38:56, 2024kb, 0ms, 203b
#include <iostream>
#include <string>

using namespace std;

int main()
{
  int T;
  string str;
  cin>>T;
  for(int i=0;i<T;i++) {
   cin>>str;
   cout<<str.front()<<str.back()<<"\n";
  }
  return 0;
}

