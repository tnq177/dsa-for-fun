/*
ID: tnguye21
LANG: C
TASK: beads
*/

#include <stdio.h>
#include <stdlib.h>

int main () {
    FILE *fin  = fopen ("beads.in", "r");
    FILE *fout = fopen ("beads.out", "w");

    int N;
    int i;
    char *necklace = NULL;

    fscanf(fin, "%d", &N);
    
    necklace = malloc(sizeof(char) * N);
    fscanf(fin, "%s", necklace);

    int max_len = -1;

    for (i = 0; i < N; i++) {
        int left_start = i;
        int right_start = i + 1 < N ? i + 1 : 0;

        char char_left = necklace[left_start];
        char char_right = necklace[right_start];

        int len = 2;
        int go_left = 1;
        int go_right = 1;
        while (go_left && go_right) {
            if (go_left) {
                left_start = left_start - 1 >= 0 ? left_start - 1 : N - 1;
                if (left_start == right_start) {
                    break;
                }

                if (necklace[left_start] == 'w') {
                    len ++;
                }
                else {
                    if (char_left == 'w') {
                        char_left = necklace[left_start];
                        len ++;
                    }
                    else {
                        if (necklace[left_start] == char_left) {
                            len ++;
                        }
                        else {
                            go_left = 0;
                            left_start = left_start + 1 < N ? left_start + 1 : 0;
                        }
                    }
                }
            }


            if (go_right) {
                right_start = right_start + 1 < N ? right_start + 1 : 0;
                if (right_start == left_start) {
                    break;
                }

                if (necklace[right_start] == 'w') {
                    len ++;
                }
                else {
                    if (char_right == 'w') {
                        char_right = necklace[right_start];
                        len ++;
                    }
                    else {
                        if (necklace[right_start] == char_right) {
                            len ++;
                        }
                        else {
                            go_right = 1;
                            right_start = right_start - 1 > 0 ? right_start - 1 : N - 1;
                        }
                    }
                }
            }
        }

        if (len > max_len) {
            max_len = len;
        }
    }

    fprintf(fout, "%d\n", max_len);

    fclose(fin);
    fclose(fout);
    return 0;
}
