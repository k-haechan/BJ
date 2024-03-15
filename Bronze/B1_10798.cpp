# 세로읽기, 2023년 4월 16일 10:52:14, 2020kb, 0ms, 270b
#include <iostream>

using namespace std;
char word[5][16];

int main()
{

	for (int i = 0; i < 5; i++) {
		cin.getline(word[i], 16);
	}

	for (int c = 0; c < 15; c++) {
		for (int r = 0; r < 5; r++) {
			if (word[r][c] != 0)
				cout << word[r][c];
		}
	}

	return 0;
}
