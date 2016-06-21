/*
ID: tnguye21
LANG: C
TASK: sort3
*/

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return ( *(int*)a - *(int*)b );
}

int main () {
    FILE *fin  = fopen ("sort3.in", "r");
    FILE *fout = fopen ("sort3.out", "w");

    int N;
    int* list;
    int swap = 0;
    int i, j;
    int A1 = 0;
    int A2 = 0;
    int A3 = 0;

    fscanf(fin, "%d", &N);

    list = malloc(sizeof(int) * N);
    for(i = 0; i < N; i++) {
        fscanf(fin, "%d", &list[i]);
        if(list[i] == 1) {
            A1++;
        }
        else if(list[i] == 2) {
            A2++;
        }
        else {
            A3++;
        }
    }    

    for(i = 0; i < A1; i++) {
        for(j = A1; j < A1 + A2; j++) {
            if(list[i] == 2 && list[j] == 1) {
                list[i] = 1;
                list[j] = 2;
                swap++;
                break;
            }
        }
    }

    for(i = 0; i < A1; i++) {
        for(j = A1 + A2; j < A1 + A2 + A3; j++) {
            if(list[i] == 3 && list[j] == 1) {
                list[i] = 1;
                list[j] = 3;
                swap++;
                break;
            }
        }
    }

    for(i = A1; i < A1 + A2; i++) {
        for(j = A1 + A2; j < A1 + A2 + A3; j++) {
            if(list[i] == 3 && list[j] == 2) {
                list[i] = 2;
                list[j] = 3;
                swap++;
                break;
            }
        }
    }

    for(i = 0; i < A1; i++) {
        if(list[i] != 1) {
            swap += 2;
        }
    }

    fprintf(fout, "%d\n", swap);
    free(list);
    fclose(fin);
    fclose(fout);
    return 0;
}
