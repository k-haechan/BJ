# 약수 구하기, 2023년 4월 17일 19:44:25, 2020kb, 0ms, 217b
#include <iostream>

using namespace std;

int main()
{
	int n, k;
	cin >> n>> k;
	for (int i = 1; i <= n; i++) {
		if (n % i == 0)
			k--;
		
		if (k == 0) {
			cout << i;
			return 0;
		}
	}
	cout << 0;
	return 0;
}
