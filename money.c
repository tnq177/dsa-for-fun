/*
ID: tnguye21
LANG: C
TASK: money
*/

#include <stdio.h>
#include <stdlib.h>

int V, N;
int* coins;
signed long long* d;

int compare(const void* a, const void* b) {
    return ( *(int*)a - *(int*)b );
}

int main () {
    FILE *fin  = fopen ("money.in", "r");
    FILE *fout = fopen ("money.out", "w");

    fscanf(fin, "%d %d", &V, &N);

    coins = malloc(sizeof(int) * (V + 1));
    coins[0] = 0;
    int i, j;
    for(i = 0; i < V; i++) {
        fscanf(fin, "%d", &coins[i + 1]);
    }
    qsort(coins, V + 1, sizeof(int), compare);

    d = malloc(sizeof(signed long long) * (N + 1));
    d[0] = 1;
    for(i = 1; i <= N; i++) {
        d[i] = 0;
    }

    for(i = 1; i <= V; i++) {
        for(j = coins[i]; j <= N; j++) {
            d[j] += d[j - coins[i]];
        }
    }

    fprintf(fout, "%llu\n", d[N]);
    free(coins);
    free(d);
    fclose(fin);
    fclose(fout);
    return 0;
}
