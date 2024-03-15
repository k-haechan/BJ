# 약수들의 합, 2023년 4월 17일 19:31:01, 2064kb, 0ms, 695b
#include <iostream>
#include <string.h>
#include <cmath>

using namespace std;
int arr[10000];
int offset;
int arr2[1000];
void nPerfect(int n) {
	for (int i = 1; i < n; i++) {
		if (n % i == 0) {
			arr[offset++] = i;
		}
	}
	int sum = 0; 
	for (int i = 0; i < offset; i++) {

		sum += arr[i];
		//cout << arr[i] << '\n';
	}
	if (sum == n) {
		cout << sum << " = ";
		for (int i = 0; i < offset-1; i++)
			cout << arr[i]<<" + ";
		cout << arr[offset-1] << '\n';
		memset(arr, 0, 10000);
		offset = 0;
		return;
	}
	cout << n << " is NOT perfect.\n";
	memset(arr, 0, 10000);
	offset = 0;
}
int main()
{
	int N=1;
	while (1) {
		cin >> N;
		if (N == -1)
			break;
		nPerfect(N);
	}

	return 0;
}

