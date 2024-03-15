# 분수 합, 2023년 4월 18일 22:43:27, 2020kb, 0ms, 408b
#include <iostream>
#include <cmath>
using namespace std;

/*
gcd(a,b) = gcd(b,a%b)
*/
int gcd(int a, int b) {
	int tmp;
	if (a < b) {
		tmp = a;
		a = b;
		b = tmp;
	}

	while (b != 0) {
		tmp = a;
		a = b;
		b = tmp % b;
	}
	return a;
}

int main()
{
	int a, b, c, d;
	cin >> a >> b >> c >> d;
	int x, y;
	y = a * d + b * c;
	x = b * d;
	int g = gcd(x, y);
	
	cout << y / g << " " << x / g;
	
	return 0;
}

