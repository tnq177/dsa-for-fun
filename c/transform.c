/*
ID: tnguye21
LANG: C
TASK: transform
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void rotate_90(char *str, int N, char *result) {
    char* temp = NULL;
    int i, x, y;
    int len;

    len = N * N;
    temp = malloc(sizeof(char) * (len + 1));
    for (i = 0; i < len; i++) {
        x = i / N;
        y = N - 1 - i % N;

        temp[i] = str[y * N + x];
    }
    temp[N * N] = '\0';

    strcpy(result, temp);
    free(temp);
}

void rotate_180(char *str, int N, char *result) {
    rotate_90(str, N, result);
    rotate_90(result, N, result);
}

void rotate_270(char *str, int N, char *result) {
    rotate_90(str, N, result);
    rotate_180(result, N, result);
}

void reflect(char* str, int N, char *result) {
    char* temp;
    int r, c;

    temp = malloc(sizeof(char) * (N * N + 1));
    for (r = 0; r < N; r++) {
        for (c = 0; c < N; c++) {
            temp[r * N + c] = str[r * N + (N - 1 - c)];
        }
    }

    temp[N * N] = '\0';
    strcpy(result, temp);
    free(temp);
}

void comb_1(char* str, int N, char *result) {
    reflect(str, N, result);
    rotate_90(result, N, result);
}

void comb_2(char* str, int N, char *result) {
    reflect(str, N, result);
    rotate_180(result, N, result);
}

void comb_3(char* str, int N, char *result) {
    reflect(str, N, result);
    rotate_270(result, N, result);
}

int main () {
    FILE *fin  = fopen ("transform.in", "r");
    FILE *fout = fopen ("transform.out", "w");

    char *before    = NULL;
    char *after     = NULL;
    int N;
    int i;

    fscanf(fin, "%d", &N);
    before  = malloc(sizeof(char) * (N * N + 1));
    after   = malloc(sizeof(char) * (N * N + 1));

    for (i = 0; i < N; i++) {
        fscanf(fin, "%s", &before[i * N]);
    }
    before[N * N] = '\0';
    for (i = 0; i < N; i++) {
        fscanf(fin, "%s", &after[i * N]);
    }
    after[N * N] = '\0';

    char* result;
    result = malloc(sizeof(char) * (N * N + 1));

    for (;;) {
        rotate_90(before, N, result);
        if (!strcmp(after, result)) {
            i = 1;
            break;
        }
    
        rotate_180(before, N, result);
        if (!strcmp(after, result)) {
            i = 2;
            break;
        }
    
        rotate_270(before, N, result);
        if (!strcmp(after, result)) {
            i = 3;
            break;
        }

        reflect(before, N, result);
        if (!strcmp(after, result)) {
            i = 4;
            break;
        }

        comb_1(before, N, result);
        if (!strcmp(after, result)) {
            i = 5;
            break;
        }

        comb_2(before, N, result);
        if (!strcmp(after, result)) {
            i = 5;
            break;
        }

        comb_3(before, N, result);
        if (!strcmp(after, result)) {
            i = 5;
            break;
        }

        strcpy(result, before);
        if (!strcmp(after, result)) {
            i = 6;
            break;
        }

        i = 7;
        break;
    }

    fprintf(fout, "%d\n", i);

    fclose(fin);
    fclose(fout);
    free(before);
    free(after);
    free(result);
    return 0;
}
