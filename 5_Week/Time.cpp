#include <bits/stdc++.h>

using namespace std;
int h, cnt;
// 특정한시각안에'3'이포함되어있는지의여부
bool check(int h, int m, int s) {
	if (h % 10== 3|| m / 10== 3|| m % 10== 3|| s / 10== 3|| s % 10== 3)
		return true;
	return false;
}

int main(void) {
// H 입력받기
	cin>> h;
	for(int i= 0; i<= h; i++) {
		for(int j = 0; j < 60; j++) {
			for(int k = 0; k < 60; k++) {
				if(check(i, j, k)) cnt++;
			}
		}
	}
	cout<< cnt<< '\n';
	return 0;
}
