# 가로수, 2023년 4월 18일 23:13:32, 2020kb, 56ms, 468b
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
	int n,x,min,d,tmp;
	cin >> n;
	
	cin >> x;
	min = x;
    d = x;
	cin >> x;;
	tmp = x;
	d = x - d;

	for (int i = 2; i < n; i++) {
		cin >> x;
		d = gcd(x - tmp, d);
	}
	
	cout<<(x - min ) / d + 1 - n;
	return 0;
}

