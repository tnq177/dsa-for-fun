/*
ID: tnguye21
LANG: C
TASK: gift1
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int lookup(char* name, char* names[], int len) {
    int i;
    for(i = 0; i < len; i++) {
        if(!strcmp(names[i], name)) {
            return i;
        }
    }

    return -1;
}

void get_two_numbers(char* str, int* a1, int* a2) {
    char *p = str;
    int count = 0;
    while (*p) {
        if (isdigit(*p)) {
            if (count == 0) {
                *a1 = strtol(p, &p, 10);
                count ++;
            }
            else {
                *a2 = strtol(p, &p, 10);
                return;
            }
        }
        else {
            p++;
        }
    }
}

int main () {
    FILE *fin  = fopen ("gift1.in", "r");
    FILE *fout = fopen ("gift1.out", "w");

    char *line = NULL;
    size_t len = 0;
    int NP;
    getline(&line, &len, fin);
    NP = atoi(line);

    char** names = malloc(sizeof(char*) * NP);
    int* remains = malloc(sizeof(int) * NP);
    int i;

    for(i = 0; i < NP; i++) {
        names[i] = malloc(sizeof(char) * 15);
        getline(&names[i], &len, fin);
        remains[i] = 0;
    }

    char *name = NULL;
    int original_amount = 0;
    int num_receivers = 0;
    int amount_received = 0;
    int j;
    for(i = 0; i < NP; i++) {
        getline(&name, &len, fin);
        getline(&line, &len, fin);

        get_two_numbers(line, &original_amount, &num_receivers);

        if(num_receivers > 0) {
            remains[lookup(name, names, NP)] += original_amount % num_receivers - original_amount;
            amount_received = original_amount / num_receivers;
            for(j = 0; j < num_receivers; j++) {
                getline(&name, &len, fin);
                remains[lookup(name, names, NP)] += amount_received;          
            } 
        }
        else {
            remains[lookup(name, names, NP)] += original_amount;
        }
    }   

    for(i = 0; i < NP; i++) {
        names[i][strlen(names[i]) - 1] = '\0';
        fprintf(fout, "%s %d\n", names[i], remains[i]);
    }

    fclose(fin);
    fclose(fout);
    free(remains);
    free(names);
    return 0;
}
