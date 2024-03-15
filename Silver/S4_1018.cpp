# 체스판 다시 칠하기, 2023년 4월 18일 21:38:30, 2024kb, 0ms, 871b
#include <iostream>

using namespace std;

char arr[50][50];

int main()
{

	int n, m;
	cin >> n >> m;
	cin.ignore(); // cin 후 개행ㅇ

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	int tmp, cnt, min_n=32; 

	for (int r = 0; r + 7 < n; r++) {
		for (int c = 0; c + 7 < m; c++) {
			for (int t = 0; t < 2; t++) {
				if (t == 0)
					tmp = 'B';
				else
					tmp = 'W';

				cnt = 0;
				for (int i = 0; i < 8; i++) {
					for (int j = 0; j < 8; j++) {
						if ((i + j) % 2 == 0) {
							if (arr[r + i][c + j] != tmp)
								cnt++;
						}
						else {
							if (arr[r + i][c + j] == tmp)
								cnt++;
						}

					}
				}
				if (cnt < min_n) {
					min_n = cnt;
				}
			}
			
				
		}
	}

	cout << min_n;
	return 0;
}
/*

*/
char fuck(char fu, const char xx, int i) {
	int r, c;
	r = i / 8;
	c = i % 8;

	if (fu == 'B')
		return 'W';
	else
		return 'B';
}

