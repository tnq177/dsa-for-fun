/*
ID: tnguye21
LANG: C
TASK: milk
*/

#include <stdio.h>
#include <stdlib.h>

struct farmer {
    int price;
    int amount;
};

static int compare_farmer(const void* f1, const void* f2) {
    struct farmer* p1 = (struct farmer*) f1;
    struct farmer* p2 = (struct farmer*) f2;

    return p1->price - p2->price;
}

int main () {
    FILE *fin  = fopen ("milk.in", "r");
    FILE *fout = fopen ("milk.out", "w");

    int N, M;
    fscanf(fin, "%d %d", &N, &M);

    struct farmer* farmers = NULL;
    farmers = malloc(sizeof(struct farmer) * M);

    int i;
    for(i = 0; i < M; i++) {
        fscanf(fin, "%d %d", &farmers[i].price, &farmers[i].amount);
    }

    qsort(farmers, M, sizeof(struct farmer), compare_farmer);

    int total_cost = 0;
    while (N > 0) {
        for(i = 0; i < M; i++) {
            int amount_to_buy = (farmers[i].amount <= N) ? farmers[i].amount : N;
            N -= amount_to_buy;
            total_cost += amount_to_buy * farmers[i].price;
        }
    }

    fprintf(fout, "%d\n", total_cost);

    free(farmers);
    fclose(fin);
    fclose(fout);
    return 0;
}
