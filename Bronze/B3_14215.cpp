# 세 막대, 2023년 4월 17일 20:50:53, 2020kb, 0ms, 328b
#include <iostream>

using namespace std;

int main()
{
	int a[3];
	int max, sum;
	max = sum = 0;
	for (int i = 0; i < 3; i++)
		cin >> a[i];

	for (int i = 0; i < 3; i++) {
		if (a[i] > max)
			max = a[i];
		sum += a[i];
	}

	if ((max * 2) >= sum)
		cout << 2 * (sum - max) - 1 << "\n";

	else cout << sum << '\n';
	return 0;
}
