#include <stdio.h>

int visited[9]={1};
int graph[9][3] = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};

void dfs(int x) {
	visited[x] = 1;
	printf("%d ",x);
	int i=0;
	int size = sizeof(graph[x]) / sizeof(int);
	for (i=0;i<size;i++) {
	    int node = graph[x][i];
		// 인접한 노드가 방문한 적이 없다면 DFS 수행
		if(!visited[node]) {
			dfs(node);
		}
	}
}

int main(void) {
	dfs(1); 
}
