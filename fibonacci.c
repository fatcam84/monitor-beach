#include <stdio.h>

int
main() {
    int fib[10] = {0, 1};
    int i;

    for (i = 2; i < 10; i++) {
        fib[i] = fib[i - 2] + fib[i - 1];
    }

    for (i = 0; i < 10; i++) {
        printf("Number %i in the Fibonacci Sequence is %d\n", i+1, fib[i]);
    }
}
        
    
