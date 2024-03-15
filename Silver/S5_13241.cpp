# 최소공배수, 2023년 4월 18일 22:33:49, 2020kb, 0ms, 366b
#include <iostream>
#include <cmath>
using namespace std;

/*
gcd(a,b) = gcd(b,a%b)
*/
long long int gcd(long long int a,long long int b) {
	long long int tmp;
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
	long long int a, b;
	cin >> a >> b;
	cout << a*b/gcd(a, b);
	return 0;
}

