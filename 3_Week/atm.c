#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    return(*(int*)a - *(int*)b);
}

int main() {
	int answer=0,n,i=0;
	scanf("%d",&n);
	int P[n+1];
	P[0]=0;
	for(i=1;i<=n;i++){
	    scanf("%d",&P[i]);
	}
	qsort(P, sizeof(P) / sizeof(int), sizeof(int), compare);
	
	for(i=1;i<=n;i++){
	    P[i]=P[i-1]+P[i];
	    answer+=P[i];
	}
	printf("%d",answer);
	return 0;
}
