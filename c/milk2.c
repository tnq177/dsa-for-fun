/*
ID: tnguye21
LANG: C
TASK: milk2
*/

#include <stdio.h>
#include <stdlib.h>

struct node {
    int time;
    int type;
};

static int compare_nodes(const void *p1, const void *p2) {
    struct node* n1 = (struct node*) p1;
    struct node* n2 = (struct node*) p2;

    return n1->time - n2->time;
}

int main () {
    FILE *fin  = fopen ("milk2.in", "r");
    FILE *fout = fopen ("milk2.out", "w");

    int N;
    int start, end;
    int i;
    struct node* nodes = NULL;

    fscanf(fin, "%d", &N);
    nodes = malloc(sizeof(struct node) * 2 * N);

    for (i = 0; i < N; i++) {
        fscanf(fin, "%d %d", &start, &end);

        nodes[2 * i].time = start;
        nodes[2 * i].type = 1;

        nodes[2 * i + 1].time = end;
        nodes[2 * i + 1].type = 0;
    }

    qsort(nodes, 2 * N, sizeof(struct node), compare_nodes);

    int max_cont_interval = -1;
    int max_idle_interval = 0;
    int max_start = nodes[0].time;
    int count = 1;
    int pre_count = 1;

    int cont_interval = 0;
    int idle_interval = 0;

    for (i = 1; i < 2 * N; i++) {
        pre_count = count;

        if (nodes[i].type) {
            count++;
        }
        else {
            count--;
        }

        if (!count) {
            if (i < 2 * N - 1 && nodes[i].time == nodes[i + 1].time && nodes[i + 1].type) {
                continue;
            }
            else {
                cont_interval = nodes[i].time - max_start;
                if (cont_interval > max_cont_interval) {
                    max_cont_interval = cont_interval;
                }

                if (i < 2 * N - 1) {
                    max_start = nodes[i + 1].time;
                } 
            }
        }
        else if (count == 1 && !pre_count) {
            idle_interval = nodes[i].time - nodes[i - 1].time;
            if (idle_interval > max_idle_interval) {
                max_idle_interval = idle_interval;
            }
        }
    }
    fprintf(fout, "%d %d\n", max_cont_interval, max_idle_interval);
    free(nodes);
    fclose(fin);
    fclose(fout);
    return 0;
}
