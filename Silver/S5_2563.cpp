# 색종이, 2023년 4월 16일 11:12:14, 2060kb, 0ms, 378b
#include <iostream>

using namespace std;

int arr[100][100];

int main()
{
	int n,r,c,cnt=0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> r>> c;
		for (int x = r; x < r+10; x++) 
			for (int y = c; y < c + 10; y++) 
				arr[x][y] = 1;
			
		
	}

	for (r = 0; r < 100; r++)
		for (c = 0; c < 100; c++)
			if (arr[r][c] == 1)
				cnt++;
	cout << cnt << '\n';

	return 0;
}
