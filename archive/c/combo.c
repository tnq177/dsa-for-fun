/*
ID: tnguye21
LANG: C
TASK: combo
*/

#include <stdio.h>
#include <stdlib.h>

void get_set(int a, int N, int** set, int* len) {
    *len = 0;
    *set = malloc(sizeof(int) * 5);

    int i, j, _i, existed;
    for(i = a - 2; i < a + 3; i++) {
        _i = i;
        while(_i < 1) {
            _i += N;
        }
        while(_i > N) {
            _i -= N;
        }

        existed = 0;
        for(j = 0; j < (*len); j++) {
            if ((*set)[j] == _i) {
                existed = 1;
            }
        }

        if (!existed) {
            (*set)[(*len)] = _i;
            (*len)++;
        }
    }
}

int count_overlap(int* set1, int* set2, int len1, int len2) {
    int i, j;
    int count = 0;
    for(i = 0; i < len1; i++) {
        for(j = 0; j < len2; j++) {
            if(set1[i] == set2[j]) {
                count++;
            }
        }
    }

    return count;
}

int main () {
    FILE *fin  = fopen ("combo.in", "r");
    FILE *fout = fopen ("combo.out", "w");

    int N;
    int a[6] = {0, 0, 0, 0, 0, 0};
    int i;

    fscanf(fin, "%d", &N);
    for(i = 0; i < 6; i++) {
        fscanf(fin, "%d", &a[i]);
    }

    int** sets;
    int* lens;
    sets = malloc(sizeof(int*) * 6);
    lens = malloc(sizeof(int) * 6);
    for(i = 0; i < 6; i++) {
        get_set(a[i], N, &sets[i], &lens[i]);
    }

    int overlap;
    overlap = count_overlap(sets[0], sets[3], lens[0], lens[3]);
    overlap *= count_overlap(sets[1], sets[4], lens[1], lens[4]);
    overlap *= count_overlap(sets[2], sets[5], lens[2], lens[5]);

    fprintf(fout, "%d\n", lens[0] * lens[1] * lens[2] + lens[3] * lens[4] * lens[5] - overlap);

    free(sets);
    free(lens);
    fclose(fin); 
    fclose(fout);
    return 0;
}
