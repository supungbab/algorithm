#include <bits/stdc++.h>

using namespace std;

int n;

string plans;
int x = 1, y = 1;

// L, R, U, D에따른이동방향
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char moveTypes[4] = {'L', 'R', 'U', 'D'};

int main(void) {
	cin >> n;
	cin.ignore(); // 버퍼비우기

	getline(cin, plans);
	// 이동계획을하나씩확인하기
	for(int i= 0; i< plans.size(); i++) {
		char plan = plans[i];
		// 이동후좌표구하기
		int nx= -1, ny= -1;
		for(int j = 0; j < 4; j++) {
			if(plan == moveTypes[j]) {
				nx= x + dx[j];
				ny= y + dy[j];
			}
		}
		// 공간을벗어나는경우무시
		if(nx < 1|| ny < 1|| nx > n || ny > n) continue;
		// 이동수행
		x = nx;
		y = ny;
	}
	cout << x << ' ' << y << '\n';
	return 0;
}
