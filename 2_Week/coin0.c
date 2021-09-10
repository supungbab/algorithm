#include <stdio.h>

int main() {
	int answer=0,k,n,i=0;
	scanf("%d %d",&n,&k);
	int coins[n];
	
	for(i=0;i<n;i++)
	    scanf("%d",&coins[i]);
	    
	int count=0;
	while(k!=0){
	    int coin=coins[--i];
	    answer+=k/coin;
	    k%=coin;
	}
	printf("%d",answer);
	return 0;
}
