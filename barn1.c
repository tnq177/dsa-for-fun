/*
ID: tnguye21
LANG: C
TASK: barn1
*/

/*
My first algorithm is to split the sorted sequence of barn numbers into M-1 
subsequences. For a given sequence, split it at the point which minimizes the
total difference between two resulting subsequences. Repeat this for the largest
sequence until total split reaches M-1. Obviously, it's not correct. 

I looked up this gap solution online and it sounds correct...
*/
#include <stdio.h>
#include <stdlib.h>

struct gap {
    int start;
    int end;
    int len;
};

int compare(const void* a, const void* b) {
    return ( *(int*)a - *(int*)b );
}

int compare_gap(const void* a, const void* b) {
    return ((struct gap*) a)->len - ((struct gap*) b)->len;
}

int main () {
    FILE *fin  = fopen ("barn1.in", "r");
    FILE *fout = fopen ("barn1.out", "w");

    int M, S, C;
    int* barns = NULL;
    struct gap* gaps = NULL;

    fscanf(fin, "%d %d %d\n", &M, &S, &C);

    barns = malloc(sizeof(int) * C);
    int i;
    for(i = 0; i < C; i++) {
        fscanf(fin, "%d\n", &barns[i]);
    }
    qsort(barns, C, sizeof(int), compare);

    gaps = malloc(sizeof(struct gap) * (C - 1));
    for(i = 0; i < C - 1; i++) {
        gaps[i].start = barns[i];
        gaps[i].end = barns[i + 1];
        gaps[i].len = barns[i + 1] - barns[i];
    }
    qsort(gaps, C - 1, sizeof(struct gap), compare_gap);

    if (M >= C) {
        fprintf(fout, "%d\n", C);
    }
    else {
        int total_cost = barns[C - 1] - barns[0] + 1;
        for(i = 0; i < M - 1; i++) {
            total_cost -= gaps[C - 2 - i].len - 1;
        }
        fprintf(fout, "%d\n", total_cost);
    }

    free(barns);
    free(gaps);
    fclose(fin);
    fclose(fout);
    return 0;
}
