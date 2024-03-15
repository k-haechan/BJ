# 행렬 덧셈, 2023년 4월 14일 21:05:28, 2060kb, 4ms, 394b
#include <iostream>

using namespace std;
int mat[100][100];	// 40000
int main()
{
	int n, m, tmp;
	cin >> n >> m;
	for (int i = 0; i < 2; i++) {
		for (int r = 0; r < n; r++) {
			for (int c = 0; c < m; c++) {
				cin >> tmp;
				mat[r][c] += tmp;
			}
		}
	}

	for (int r = 0; r < n; r++) {
		for (int c = 0; c < m; c++) {
			cout << mat[r][c] << " ";
		}
		cout << "\n";
	}
		
	
	return 0;
}
