/*
ID: tnguye21
LANG: C
TASK: dualpal
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* ten_to_B(int x, int B) {
    int len = 20;
    char* temp = malloc(sizeof(char) * len);
    temp[len - 1] = '\0';

    int idx = len - 2;
    int remainder;
    while (x != 0) {
        remainder = x % B;
        x /= B;

        if (remainder >= 10) {
            temp[idx] = remainder - 10 + 'A';
        }
        else {
            temp[idx] = remainder - 0 + '0';
        }   
        idx--;
    }

    char* result = malloc(sizeof(char) * (len - idx + 1));
    strcpy(result, &temp[idx + 1]);
    free(temp);

    return result;
}

int is_palidrome(char* x) {
    int len = strlen(x);

    if (len == 1) {
        return 1;
    }

    int i;
    for (i = 0; i <= len / 2; i++) {
        if (x[i] != x[len - 1 - i]) {
            return 0;
        }
    }

    return 1;
}

int main () {
    FILE *fin  = fopen ("dualpal.in", "r");
    FILE *fout = fopen ("dualpal.out", "w");    

    int N, S;
    fscanf(fin, "%d %d", &N, &S);

    int count = 0;
    int i;
    for (i = S + 1; ; i++) {
        int base;
        int pal_count;

        pal_count = 0;
        for (base = 2; base <= 10; base++) {
            char* i_base = ten_to_B(i, base);

            if (is_palidrome(i_base)) {
                pal_count++;
            }

            free(i_base);
            if (pal_count > 1) {
                break;
            }
        }

        if (pal_count > 1) {
            fprintf(fout, "%d\n", i);
            count ++;
        }

        if (count >= N) {
            break;
        }
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
