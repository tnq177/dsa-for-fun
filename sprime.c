/*
ID: tnguye21
LANG: C
TASK: sprime
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int N;
int prime;
char buff[9];
FILE *fin;
FILE *fout;

int compare(const void* a, const void* b) {
    return ( *(long*)a - *(long*)b );
}

int is_prime(long x) {
    if(x <= 1) {
        return 0;
    }

    long i;
    for(i = 2; i * i <= x; i++) {
        if(x % i == 0) {
            return 0;
        }
    }
    return 1;
}

void gen(int i) {
    if (i == N) {
        prime = atoi(buff);
        if(is_prime(prime)) {
            fprintf(fout, "%d\n", prime);
        }    

        return;
    }

    for(int j = 1; j <= 9; j += 2) {
        buff[i] = j - 0 + '0';
        buff[i + 1] = '\0';
        if(is_prime(atoi(buff))) {
            gen(i + 1);
        }
    }
}

int main () {
    fin  = fopen ("sprime.in", "r");
    fout = fopen ("sprime.out", "w");

    fscanf(fin, "%d", &N);
    buff[N] = '\0';

    buff[0] = '2';
    gen(1);
    buff[0] = '3';
    gen(1);
    buff[0] = '5';
    gen(1);
    buff[0] = '7';
    gen(1);

    fclose(fin);
    fclose(fout);
    return 0;
}
