/*
ID: tnguye21
LANG: C
TASK: nocows
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int N, K;
int** d;
int MOD = 9901;

int get_count(int n, int k) {
    if(d[n][k] != -1) {
        return d[n][k];
    } 

    if(n == 0 || k == 0) {
        d[n][k] = 0;
        return 0;
    }
    if(n == 1) {
        return 1;
    }

    int result = 0;
    int i;
    for(i = 1; i < n - 1; i += 2) {
        int left = get_count(i, k - 1) % MOD;
        int right = get_count(n - 1 - i, k - 1) % MOD;

        result = (result + left * right) % MOD;
    }

    d[n][k] = result;
    return result;
}

int main () {
    FILE *fin  = fopen ("nocows.in", "r");
    FILE *fout = fopen ("nocows.out", "w");    

    fscanf(fin, "%d %d", &N, &K);

    d = malloc(sizeof(int*) * (N + 1));
    int i, j;
    for(i = 0; i < N + 1; i++) {
        d[i] = malloc(sizeof(int) * (K + 1));
        for(j = 0; j < K + 1; j++) {
            d[i][j] = -1;
        }
    }

    fprintf(fout, "%d\n", (MOD + get_count(N, K) - get_count(N, K - 1)) % MOD);
    for(i = 0; i < N + 1; i++) {
        free(d[i]);
    }
    free(d);
    fclose(fin);
    fclose(fout);
    return 0;
}
