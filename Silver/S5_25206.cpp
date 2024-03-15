# 너의 평점은, 2023년 4월 13일 03:23:09, 2080kb, 0ms, 821b
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

double score(string gr) {
	if (gr == "A+")
		return 4.5;
	else if (gr == "A0")
		return 4.0;
	else if (gr == "B+")
		return 3.5;
	else if (gr == "B0")
		return 3.0;
	else if (gr == "C+")
		return 2.5;
	else if (gr == "C0")
		return 2.0;
	else if (gr == "D+")
		return 1.5;
	else if (gr == "D0")
		return 1.0;
	else if (gr == "F")
		return 0;
	return -1;
}

int main()
{
	string str,grade,tno;
	double credit, averageGrade = 0;
	int n, sum;
	n=sum=0;
	
	for (int i = 0; i < 20; i++) {
		getline(cin, str);
		istringstream ss(str);
		ss.ignore(60, ' ');
		ss >>credit >> grade;
		if (grade == "P")
			continue;
		sum += credit;
		averageGrade += score(grade)*credit;
		n++;
	}
	averageGrade /= sum;
	cout << averageGrade << "\n";
	return 0;
}

