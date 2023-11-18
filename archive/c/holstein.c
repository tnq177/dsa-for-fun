/*
ID: tnguye21
LANG: C
TASK: holstein
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main () {
    FILE *fin  = fopen ("holstein.in", "r");
    FILE *fout = fopen ("holstein.out", "w");

    int V, G;
    int* requires;
    int** scoops;
    int i, j, k;

    fscanf(fin, "%d", &V);
    
    requires = malloc(sizeof(int) * V);
    for(i = 0; i < V; i++) {
        fscanf(fin, "%d", &requires[i]);
    }

    fscanf(fin, "%d", &G);

    scoops = malloc(sizeof(int*) * G);
    for(i = 0; i < G; i++) {
        scoops[i] = malloc(sizeof(int) * V);
        for(j = 0; j < V; j++) {
            fscanf(fin, "%d", &scoops[i][j]);
        }
    }

    int min_scoops_count = 1000000;
    int min_subset_idx = -1;
    int scoops_count;
    int use_this_scoop;
    int subset_idx;
    int pass_reqs;

    int* values;
    values = malloc(sizeof(int) * V);

    int max_subset = (int) pow(2.0, (double) G);
    for(i = 0; i < max_subset; i++) {
        for(j = 0; j < V; j++) {
            values[j] = 0;
        }

        subset_idx = i;
        scoops_count = 0;
        for(j = 0; j < G; j++) {
            use_this_scoop = subset_idx % 2;
            subset_idx /= 2;

            if(use_this_scoop) {
                scoops_count++;
                for(k = 0; k < V; k++) {
                    values[k] += scoops[j][k];
                }
            }
        }

        pass_reqs = 1;
        for(j = 0; j < V; j++) {
            if(values[j] < requires[j]) {
                pass_reqs = 0;
                break;
            }
        }

        if(pass_reqs) {
            if(scoops_count < min_scoops_count) {
                min_scoops_count = scoops_count;
                min_subset_idx = i;
            }
        }
    }

    fprintf(fout, "%d", min_scoops_count);
    for(i = 0; i < G; i++) {
        use_this_scoop = min_subset_idx % 2;
        min_subset_idx /= 2;

        if(use_this_scoop) {
            fprintf(fout, " %d", i + 1);
        }
    }
    fprintf(fout, "\n");
    free(requires);
    free(scoops);
    fclose(fin);
    fclose(fout);
    return 0;
}
