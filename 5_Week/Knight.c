#include <stdio.h>

char inputData[3];
// 나이트가 이동할 수 있는 8가지 방향정의

int dx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
int dy[] = {-1, -2, -2, -1, 1, 2, 2, 1};

int main(void) {
	// 현재나이트의위치입력받기
	scanf("%s",inputData);
	int row = inputData[1] -'0';
	int column = inputData[0] -'a'+ 1;
	// 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
	int result = 0;
	for(int i= 0; i< 8; i++) {
		// 이동하고자하는위치확인
		int nextRow= row + dx[i];
		int nextColumn= column + dy[i];
		// 해당 위치로 이동이 가능하다면 카운트 증가
		if(nextRow >= 1 && nextRow <= 8 && nextColumn >= 1 && nextColumn <= 8) {
			result += 1;
		}
	}
	printf("%d",result);
	return 0;
}
