/*
ID: tnguye21
LANG: C
TASK: ride
*/

#include <stdio.h>
#include <stdlib.h>

int get_remainder(char *name) {
    int i;
    int remainder = 1;

    for (i = 0; name[i] != '\n'; i++) {
        remainder *= (name[i] - 'A' + 1);
    }

    return remainder % 47;
}

int main () {
    FILE *fin  = fopen ("ride.in", "r");
    FILE *fout = fopen ("ride.out", "w");

    char *comet = NULL;
    char *group = NULL;
    size_t len = 0;

    getline(&comet, &len, fin);
    getline(&group, &len, fin);

    if (get_remainder(comet) == get_remainder(group)) {
        fprintf (fout, "GO\n");
    }
    else {
        fprintf (fout, "STAY\n");
    }

    return 0;
}
