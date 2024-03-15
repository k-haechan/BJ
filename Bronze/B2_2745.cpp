# 진법 변환, 2023년 4월 17일 11:24:14, 2020kb, 0ms, 268b
#include <iostream>
#include <string.h>

using namespace std;

char N[40];
int main()
{
	int B, d = 0;
	cin >> N >> B;
	for (int i = 0; i < strlen(N) ; i++) {
		d *= B;
		if (N[i] >= 65) 
			d += (N[i] - 55);
			
		else
			d += (N[i] - 48);
	}
	cout << d;
	return 0;
}
