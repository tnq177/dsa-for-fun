/*
ID: tnguye21
LANG: C
TASK: preface
*/

#include <stdio.h>
#include <stdlib.h>

char chars[] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
int count[] = {0, 0, 0, 0, 0, 0, 0};

void get_count(int x) {
    // I-0, V-1, X-2, L-3, C-4, D-5, M-6

    count[6] += x / 1000;
    x -= 1000 * (x / 1000);

    if(x >= 900) {
        count[6] += 1;
        count[4] += 1;
        x -= 900;
    }

    if(x >= 500) {
        count[5] += 1;
        x -= 500;
    }

    if(x >= 400) {
        count[5] += 1;
        count[4] += 1;
        x -= 400;
    }

    count[4] += x / 100;
    x -= 100 * (x / 100);

    if(x >= 90) {
        count[4] += 1;
        count[2] += 1;
        x -= 90;
    }

    if(x >= 50) {
        count[3] += 1;
        x -= 50;
    }

    if(x >= 40) {
        count[3] += 1;
        count[2] += 1;
        x -= 40;
    }

    count[2] += x / 10;
    x -= 10 * (x / 10);

    if(x >= 9) {
        count[2] += 1;
        count[0] += 1;
        x -= 9;
    }
    
    if(x >= 5) {
        count[1] += 1;
        x -= 5;
    }

    if(x >= 4) {
        count[1] += 1;
        count[0] += 1;
        x -= 4;
    }

    count[0] += x;
}

int main () {
    FILE *fin  = fopen ("preface.in", "r");
    FILE *fout = fopen ("preface.out", "w");

    int N;
    fscanf(fin, "%d", &N);

    int i;
    for(i = 1; i <= N; i++) {
        get_count(i);
    }

    int highest_letter_idx = 0;
    for(i = 6; i >= 0; i--) {
        if(count[i] != 0) {
            highest_letter_idx = i;
            break;
        }
    }

    for(i = 0; i <= highest_letter_idx; i++) {
        fprintf(fout, "%c %d\n", chars[i], count[i]);
    }

    fclose(fin);    
    fclose(fout);    
    return 0;
}
