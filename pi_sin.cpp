#include <stdio.h>

#define STEPCOUNTER 1000000000

int main(void) {
    long i;
    double pi = 0;

    for (i = 0; i < STEPCOUNTER; i++) {
        pi += 1.0 / (i * 4.0 + 1.0);
        pi -= 1.0 / (i * 4.0 + 3.0);
    }

    pi = pi * 4.0;
    printf("PI = %2.16lf\n", pi);

    return 0;
}
