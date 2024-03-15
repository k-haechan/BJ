# 최댓값, 2023년 4월 14일 21:14:55, 2020kb, 0ms, 324b
#include <iostream>

using namespace std;

int main()
{
	int max = 0, row, col, input;
	for (int r = 0; r < 9; r++) {
		for (int c = 0; c < 9; c++) {
			cin >> input;
			if (input >= max) {
				max = input;
				row = r+1;
				col = c+1;
			}
		}
	}

	cout << max << "\n";
	cout << row << " " << col << "\n";		
	
	return 0;
}
