#include <stdio.h>

/* print Fahrenheit-Celcius table
   for fahr = 0, 20, ..., 300 */

float conversion(float fahr);

int
main() {
    float fahr;
    int lower, upper, step;

    lower = 0;       /* lower limit of temp table*/
    upper = 100;     /* upper limit */
    step = 2;       /* step size */
    
    printf("This is the Fahrenheit-Celsius conversion table\n");
    for (fahr = lower; fahr < upper; fahr = fahr + step)
            printf("%3.0f %6.1f\n", fahr, conversion(fahr));
}

/* conversion: convert fahr into celsius */
float
conversion(float fahr) {

    return (5.0/9.0) * (fahr - 32.0);
}
