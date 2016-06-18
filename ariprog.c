/*
ID: tnguye21
LANG: C
TASK: ariprog
*/

// Yes, it's ugly
#include <stdio.h>
#include <stdlib.h>

int main () {
    FILE *fin  = fopen ("ariprog.in", "r");
    FILE *fout = fopen ("ariprog.out", "w");

    int N, M;
    fscanf(fin, "%d", &N);
    fscanf(fin, "%d", &M);

    int* bisquares;
    int* is_bisquares;
    int count;
    int i, j, p, q;

    int length = 0;
    is_bisquares = malloc(sizeof(int) * ((M + 1) * (M + 1) * 2 + 1));

    for(p = 0; p <= M; p++) {
        for(q=0; q <= M; q++) {
            if (!is_bisquares[p*p + q*q]) {
                is_bisquares[p*p + q*q] = 1;
                length++;
            }
        }
    }

    bisquares = malloc(sizeof(int) * length);
    count = 0;
    for(i = 0; i < (M + 1) * (M + 1) * 2 + 1; i++) {
        if(is_bisquares[i]) {
            bisquares[count] = i;
            count++;
        }
    }

    int has_sequence = 0;
    int max_gap = 2 * M * M / (N - 1);
    int gap, seq_len, a;
    for(gap = 1; gap <= max_gap; gap++) {
        for(i = 0; i < count; i++) {
            a = bisquares[i];
            if(a + (N - 1)*gap > bisquares[count - 1]) {
                break;
            }

            seq_len = 1;
            for(j = 1; j < N; j++) {
                if(is_bisquares[a + j * gap]) {
                    seq_len++;
                }
                else {
                    break;
                }
            }

            if(seq_len == N) {
                has_sequence = 1;
                fprintf(fout, "%d %d\n", a, gap);
            }
        }
    }

    if(!has_sequence) {
        fprintf(fout, "NONE\n");
    }

    free(is_bisquares);
    free(bisquares);
    fclose(fin);
    fclose(fout);
    return 0;
}
