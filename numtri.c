/*
ID: tnguye21
LANG: C
TASK: numtri
*/

#include <stdio.h>
#include <stdlib.h>

int max(int x, int y) {
    return x > y ? x : y;
}

int main () {
    FILE *fin  = fopen ("numtri.in", "r");
    FILE *fout = fopen ("numtri.out", "w");    

    int R;
    int** tri;
    int** max_sum;

    fscanf(fin, "%d", &R);

    int i, j;
    tri = malloc(sizeof(int*) * R);
    max_sum = malloc(sizeof(int*) * R);
    for(i = 0; i < R; i++) {
        tri[i] = malloc(sizeof(int) * R);
        max_sum[i] = malloc(sizeof(int) * R);
    }

    for(i = 0; i < R; i++) {
        for(j = 0; j < i + 1; j++) {
            fscanf(fin, "%d", &tri[i][j]);
        }
    }

    max_sum[0][0] = tri[0][0];
    for(i = 1; i < R; i++) {
        for(j = 0; j < i + 1; j++) {
            if(!j) {
                max_sum[i][j] = max_sum[i - 1][j] + tri[i][j];
            }    
            else if(j == i) {
                max_sum[i][j] = max_sum[i - 1][i - 1] + tri[i][j];
            }
            else {
                max_sum[i][j] = max(max_sum[i - 1][j - 1], max_sum[i - 1][j]) + tri[i][j];
            }
        }
    }

    int max_value = -1;
    for(i = 0; i < R; i++) {
        if(max_sum[R - 1][i] > max_value) {
            max_value = max_sum[R - 1][i];
        }
    }

    fprintf(fout, "%d\n", max_value);
    free(tri);
    free(max_sum);
    fclose(fin);
    fclose(fout);
    return 0;
}
