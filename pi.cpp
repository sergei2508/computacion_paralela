#include <stdio.h>

#ifdef _OPENMP
#include <omp.h>
#endif

#define STEPCOUNTER 1000000000

int main(void) {
    long i;
    double pi = 0;
    int threads = 0;

#ifdef _OPENMP
    threads = omp_get_num_threads();
#endif

    printf("threads %d\n", threads);

#pragma omp parallel for reduction(+:pi)
    for (i = 0; i < STEPCOUNTER; i++) {
        pi += 1.0 / (i * 4.0 + 1.0);
        pi -= 1.0 / (i * 4.0 + 3.0);
    }

    pi = pi * 4.0;
    printf("PI = %2.16lf\n", pi);

    return 0;
}
