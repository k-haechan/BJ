# 진법 변환 2, 2023년 4월 17일 14:25:27, 2020kb, 0ms, 288b
#include <iostream>
#include <string.h>

using namespace std;

char N[40];

int main()
{
	int B, d = 0;
	cin >> d >> B;
	int i = 0;
	while (d != 0) {
		N[i++] = (d % B);
		d /= B;
	}
	while (i-- >0) {
		if (N[i] >= 10)
			N[i] += 55;
		else
			N[i] += 48;
		cout << N[i];
	}
	return 0;
}

