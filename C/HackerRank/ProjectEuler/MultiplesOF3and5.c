#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        int n; 
        scanf("%d",&n);
        
        long m3 = (n - 1)/3;
        long m5 = (n - 1)/5;
        long m15 = (n - 1)/15;
        long s = (3*m3*(m3+1)/2) + (5*m5*(m5+1)/2) - (15*m15 *(m15+1)/2);
                
        printf("%ld\n", s);
    }
    return 0;
}
