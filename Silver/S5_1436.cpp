# 영화감독 숌, 2023년 4월 18일 22:25:31, 2020kb, 60ms, 234b
#include <iostream>
#include <string>
using namespace std;

int main()
{
	string str;
	int n,i,k;
	cin >> n;

	i = 0; k = 1;
	
	while (i != n) {
		if (to_string(k++).find("666") != string::npos)
			i++;
	}
	cout << k - 1;
	return 0;
}
