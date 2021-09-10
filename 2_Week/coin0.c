#include <stdio.h>

int main() {
	int answer=0,k,n,i=0;
	scanf("%d %d",&n,&k);
	int array[n];

	for(i=0;i<n;i++){
	    scanf("%d",&array[(n-1)-i]);
	}
	int count=0;
    i=0;
    while(k!=0){
	    while(k-array[count]<0){
	        count++;
	    }
	    k=k-array[count];
	    answer++;
    }
    printf("%d",answer);
	return 0;
}
