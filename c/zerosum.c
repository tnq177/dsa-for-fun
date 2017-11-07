/*
ID: tnguye21
LANG: C
TASK: zerosum
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int get_num_digits(int x) {
    x = x ? x : 1;
    int count = 0;
    while(x) {
        count++;
        x /= 10;
    }

    return count;
}

int main () {
    FILE *fin  = fopen ("zerosum.in", "r");
    FILE *fout = fopen ("zerosum.out", "w");

    int N;
    fscanf(fin, "%d", &N);

    int max_value = (int) pow(3.0, N - 1);
    int i;
    for(i = 0; i < max_value; i++) {
        int temp = i;

        int* ops;
        int op_count = 0;
        ops = malloc(sizeof(int) * (N));

        int result = 0;
        int prev_num = 0;
        int prev_op = -1;
        int curr_op;
        int j;
        for(j = N; j >= 1; j--) {
            if(j > 1) {
                curr_op = temp % 3;
                temp /= 3;
            }
            else {
                curr_op = -1;
            }
            if(prev_op == 0) {
                prev_num = j * ((int) pow(10, get_num_digits(prev_num))) + prev_num;
            }
            else if(prev_op == -1) {
                prev_num = j;
            }
            else if(prev_op == 1) {
                result += prev_num;
                prev_num = j;
            }
            else {
                result -= prev_num;
                prev_num = j;
            }

            prev_op = curr_op;
            ops[op_count] = curr_op;
            op_count++;
        }
        result += prev_num;
        if(result == 0) {
            for(j = 1; j <= N; j++) {
                if(j == 1) {
                    fprintf(fout, "%d", j);
                }
                else {
                    char op = ' ';
                    if(ops[op_count - j] == 0) {
                        op = ' ';
                    }
                    else if(ops[op_count - j] == 1) {
                        op = '+';
                    }
                    else {
                        op = '-';
                    }
                    fprintf(fout, "%c%d", op, j);
                }
            }
            fprintf(fout, "\n");
        }
        free(ops);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
