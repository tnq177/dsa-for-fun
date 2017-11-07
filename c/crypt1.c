/*
ID: tnguye21
LANG: C
TASK: crypt1
*/

#include <stdio.h>
#include <stdlib.h>

int is_valid(int num, int* digits, int len) {
    int digit;
    int i;
    int result;

    while (num > 0) {
        digit = num % 10;
        num /= 10;

        result = 0;
        for(i = 0; i < len; i++) {
            if (digits[i] == digit) {
                result = 1;
            }
        }

        if (!result) {
            return 0;
        }
    }

    return 1;
}

int main () {
    FILE *fin  = fopen ("crypt1.in", "r");
    FILE *fout = fopen ("crypt1.out", "w");

    int N;
    int* digits;
    int i, j, k, m, n;

    fscanf(fin, "%d\n", &N);
    digits = malloc(sizeof(int) * N);
    for(i = 0; i < N; i++) {
        fscanf(fin, "%d", &digits[i]);
    }

    int total_sols = 0;
    int a, b, c, d, e, num1, par1, par2, sum;
    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            for(k = 0; k < N; k++) {
                for(m = 0; m < N; m++) {
                    for(n = 0; n < N; n++) {
                        a = digits[i];
                        b = digits[j];
                        c = digits[k];
                        d = digits[m];
                        e = digits[n];

                        num1 = a * 100 + b * 10 + c;

                        par1 = e * num1;
                        par2 = d * num1;

                        if (par1 > 999 || par2 > 999) {
                            continue;
                        }

                        sum = par2 * 10 + par1;
                        if (sum > 9999) {
                            continue;
                        }

                        if (is_valid(par1, digits, N) && is_valid(par2, digits, N) && is_valid(sum, digits, N)) {
                            total_sols++;    
                        }
                    }
                }
            }
        }
    }

    fprintf(fout, "%d\n", total_sols);
    free(digits);
    fclose(fin);
    fclose(fout);
    return 0;
}
