/*
ID: tnguye21
LANG: C
TASK: skidesign
*/

#include <stdio.h>
#include <stdlib.h>

int abs(int x) {
    return x > 0 ? x : -x;
}

int min(int x, int y) {
    return x < y ? x : y;
}

int main () {
    FILE *fin  = fopen ("skidesign.in", "r");
    FILE *fout = fopen ("skidesign.out", "w");

    int N;
    int* hills;

    fscanf(fin, "%d", &N);
    hills = malloc(sizeof(int) * N);

    int i;
    for(i = 0; i < N; i++) {
        fscanf(fin, "%d", &hills[i]);
    }

    int min_cost = 100 * 100 * 1001;
    int k, cost, diff;
    for(i = 0; i <= 83; i++) {

        cost = 0;
        for(k = 0; k < N; k++) {
            if(hills[k] > i + 17) {
                diff = hills[k] - i - 17;
            }
            else if (hills[k] < i) {
                diff = i - hills[k];
            }
            else {
                diff = 0;
            }
            cost += diff * diff;
        }
        if(cost < min_cost) {
            min_cost = cost;
        }
    }

    fprintf(fout, "%d\n", min_cost);
    free(hills);
    fclose(fin);
    fclose(fout);
    return 0;
}
