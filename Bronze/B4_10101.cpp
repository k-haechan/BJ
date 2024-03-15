# 삼각형 외우기, 2023년 4월 17일 20:02:09, 2020kb, 0ms, 354b
#include <iostream>

using namespace std;

int main()
{
	int a1, a2, a3;
	cin >> a1 >> a2 >> a3;
	if ((a1 + a2 + a3) != 180) {
		cout << "Error";
		return 0;
	}

	if ((a1 != a2) && (a2 != a3) && (a3 != a1)) {
		cout << "Scalene";
		return 0;
	}

	if ((a1 == a2) && (a2 == a3)) {
		cout << "Equilateral";
		return 0;
	}

	cout << "Isosceles";
	return 0;
}
