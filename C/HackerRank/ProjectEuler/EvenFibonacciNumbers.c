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
        long n; 
        scanf("%ld",&n);
        
        
        long fib[2];
        fib[0] = 1;
        fib[1] = 2;
        
        long f = fib[0] + fib[1];
        long sum_evens = 2;

        while (f < n) {
            if (f % 2 == 0 && f < n) {
                sum_evens += f;
            }
            fib[0] = fib[1];
            fib[1] = f;
            f = fib[0] + fib[1];
        }
        printf("%ld\n", sum_evens);
        
    }
    return 0;
}
