/*
ID: tnguye21
LANG: C
TASK: palsquare
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
    FILE *fin  = fopen ("palsquare.in", "r");
    FILE *fout = fopen ("palsquare.out", "w");    

    int B;
    fscanf(fin, "%d", &B);

    int N;
    int square;
    for (N = 1; N <= 300; N++) {
        square = N * N;
        char* square_B = ten_to_B(square, B);

        if (is_palidrome(square_B)) {
            char* N_B = ten_to_B(N, B);
            fprintf(fout, "%s %s\n", N_B, square_B);

            free(N_B);
            free(square_B);
        }
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
