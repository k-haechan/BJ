# 대지, 2023년 4월 17일 19:55:28, 2020kb, 44ms, 441b
#include <iostream>

using namespace std;

int main()
{
	int n, min_x, max_x, min_y, max_y, x, y;
	cin >> n;
	cin >> min_x >> min_y;
	if (n == 1) {
		cout << 0;
		return 0;
	}
	max_x = min_x;
	max_y = min_y;

	for (int i = 1; i < n; i++) {
		cin >> x >> y;
		if (x < min_x)
			min_x = x;
		if (x > max_x)
			max_x = x;
		if (y < min_y)
			min_y = y;
		if (y > max_y)
			max_y = y;
	}

	cout << (max_x - min_x) * (max_y - min_y);
	return 0;
}
