# 삼각형과 세 변, 2023년 4월 17일 20:33:17, 2020kb, 0ms, 621b
#include <iostream>

using namespace std;

int main()
{
	int a[3];
	int max, sum;
	while (1) {
		max = sum = 0;
		cin >> a[0] >> a[1] >> a[2];
		if (a[0] == 0 && a[1] == 0 && a[2] == 0)
			return 0;

		for (int i = 0; i < 3; i++) {
			if (a[i] > max)
				max = a[i];
			sum += a[i];
		}

		if ((max * 2) >= sum) {
			cout << "Invalid\n";
			continue;
		}

		if ((a[0] == a[1]) && (a[1] == a[2])) {
			cout << "Equilateral\n";
			continue;
		}

		else if ((a[0] != a[1]) && (a[1] != a[2]) && (a[2] != a[0])) {
			cout << "Scalene\n";
			continue;
		}

		else {
			cout << "Isosceles\n";
			continue;
		}	
	}		
	return 0;
}
