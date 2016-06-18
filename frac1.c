/*
ID: tnguye21
LANG: C
TASK: frac1
*/

#include <stdio.h>
#include <stdlib.h>

FILE *fin;
FILE *fout;
int N;

void print_middle(int n1, int d1, int n2, int d2) {
    int n_m = n1 + n2;
    int d_m = d1 + d2;

    if(d_m > N) {
        return;
    }

    print_middle(n1, d1, n_m, d_m);
    fprintf(fout, "%d/%d\n", n_m, d_m);
    print_middle(n_m, d_m, n2, d2);
}

int main () {
    fin  = fopen ("frac1.in", "r");
    fout = fopen ("frac1.out", "w");    

    fscanf(fin, "%d", &N);
    fprintf(fout, "%d/%d\n", 0, 1);
    print_middle(0, 1, 1, 1);
    fprintf(fout, "%d/%d\n", 1, 1);

    fclose(fin);
    fclose(fout);
    return 0;
}
