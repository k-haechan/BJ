# 그대로 출력하기, 2023년 4월 11일 22:37:26, 2024kb, 4ms, 152b
#include <iostream>
#include <string>


int main()
{
  
  std::string str;
  while(getline(std::cin,str)) {
    std::cout<<str<<'\n';
  }
  return 0;
}

