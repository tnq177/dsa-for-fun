// how could i come up with such a dumb solution?
/*
ID: tnguye21
LANG: C
TASK: runround
*/

#include <stdio.h>
#include <stdlib.h>

int is_run_round(unsigned long x) {
    int digits[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int visited[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    int count = 0;
    int digit;
    while(1) {
        digit = x % 10;
        if(!digit) {
            return 0;
        }

        if(visited[digit]) {
            return 0;
        }
        
        visited[digit] = 1;
        digits[count] = digit;
        count++;

        x /= 10;
        if(!x) {
            break;
        }
    }

    int i;
    for(i = 0; i < 10; i++) {
        visited[i] = 0;
    }

    int total_visited = 0;
    int current_idx = count - 1;
    int step;
    while(1) {
        digit = digits[current_idx];
        step = digit % count;
        current_idx -= step;
        current_idx = current_idx < 0 ? count + current_idx : current_idx;
        
        digit = digits[current_idx];
        if(visited[digit]) {
            return 0;
        }
        visited[digit] = 1;
        total_visited++;

        if(total_visited == count) {
            break;
        }
    }

    return 1;
}

int main () {
    FILE *fin  = fopen ("runround.in", "r");
    FILE *fout = fopen ("runround.out", "w");

    unsigned long M;
    fscanf(fin, "%lu", &M);

    unsigned long x;
    for(x = M + 1; ; x++) {
        if(is_run_round(x)) {
            fprintf(fout, "%lu\n", x);
            break;
        }
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
