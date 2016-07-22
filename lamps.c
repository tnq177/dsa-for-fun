/*
ID: tnguye21
LANG: C
TASK: lamps
*/

#include <stdio.h>
#include <stdlib.h>

char* config;
char** results;
int* on;
int* off;
int result_count;
int on_count;
int off_count;
int N;
int C;

void switch_button(int b, int count) {
    if(!count) {
        return;
    }

    int i;

    if(b == 1) {
        for(i = 0; i < N; i++) {
            config[i] = (config[i] == '0') ? '1' : '0';
        }
    }
    else if(b == 2) {
        for(i = 0; i < N; i++) {
            if(i % 2 == 0) {
                config[i] = (config[i] == '0') ? '1' : '0';
            }
        }
    }
    else if(b == 3) {
        for(i = 0; i < N; i++) {
            if(i % 2 != 0) {
                config[i] = (config[i] == '0') ? '1' : '0';
            }
        }
    }
    else {
        for(i = 0; i < N; i++) {
            if((i + 1) % 3 == 1) {
                config[i] = (config[i] == '0') ? '1' : '0';
            }
        }
    }
}

int bingo() {
    int yo = 1;
    int i;
    for(i = 0; i < on_count; i++) {
        yo = yo & (config[on[i]] == '1');
    }
    for(i = 0; i < off_count; i++) {
        yo = yo & (config[off[i]] == '0');
    }
    return yo;
}

int compare(const void* a, const void* b) {
    char** c = (char**) a;
    char** d = (char**) b;

    int i;
    for(i = 0; i < N; i++) {
        if((*c)[i] == '1' && (*d)[i] == '0') {
            return 1;
        }
        if((*c)[i] == '0' && (*d)[i] == '1') {
            return -1;
        }
    }

    return 0;
}

int main () {
    FILE *fin  = fopen ("lamps.in", "r");
    FILE *fout = fopen ("lamps.out", "w");

    fscanf(fin, "%d\n%d\n", &N, &C);

    int temp;
    on = malloc(sizeof(int) * N);
    on_count = 0;
    while(1) {
        fscanf(fin, "%d", &temp);
        if(temp == -1) {
            break;
        }
        on[on_count] = temp - 1;
        on_count++;
    }
    off = malloc(sizeof(int) * N);
    off_count = 0;
    while(1) {
        fscanf(fin, "%d", &temp);
        if(temp == -1) {
            break;
        }
        off[off_count] = temp - 1;
        off_count++;
    }

    config = malloc(sizeof(char) * N);
    int i;
    for(i = 0; i < N; i++) {
        config[i] = '1';
    }

    result_count = 0;
    results = malloc(sizeof(char*) * 16);
    for(i = 0; i < 16; i++) {
        results[i] = malloc(sizeof(char) * N);
    }

    int a,b,c,d;
    for(a = 0; a < 2; a++) {
        for(b = 0; b < 2; b++) {
            for(c = 0; c < 2; c++) {
                for(d = 0; d < 2; d++) {
                    if(C < a + b + c + d) {
                        continue;
                    }

                    switch_button(1, a);
                    switch_button(2, b);
                    switch_button(3, c);
                    switch_button(4, d);

                    if(bingo()) {
                        for(i = 0; i < N; i++) {
                            results[result_count][i] = config[i];
                        }
                        result_count++;
                    }

                    switch_button(4, d);
                    switch_button(3, c);
                    switch_button(2, b);
                    switch_button(1, a);
                }
            }
        }
    }

    if(!result_count) {
        fprintf(fout, "IMPOSSIBLE\n");
    }   
    else {
        qsort(results, result_count, sizeof(char*), compare);
        int j;
        for(i = 0; i < result_count; i++) {
            int not_visited = 1;
            for(j = 0; j < i; j++) {
                int rc = compare((const void*)&results[i], (const void *)&results[j]);
                if(rc == 0) {
                    not_visited = 0;
                }
            }
            if(not_visited) {
                for(j = 0; j < N; j++) {
                    fprintf(fout, "%c", results[i][j]);
                }
                fprintf(fout, "\n");
            }
        }
    }

    free(on);
    free(off);
    free(config);
    for(i = 0; i < 16; i++){
        free(results[i]);
    }
    free(results);
    fclose(fin);    
    fclose(fout);    
    return 0;
}
