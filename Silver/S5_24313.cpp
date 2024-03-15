# 알고리즘 수업 - 점근적 표기 1, 2023년 4월 17일 21:40:13, 2020kb, 0ms, 171b
#include <iostream>

using namespace std;

int main()
{
	int a0, a1, c, n0;
	cin >>a1 >> a0>> c >> n0;
	cout << ((a1 * n0 + a0 <= c * n0) && (c - a1 >= 0));
	
	return 0;
}
