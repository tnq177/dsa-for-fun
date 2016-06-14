/*
ID: tnguye21
LANG: C
TASK: namenum
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_digit(char x) {
    int digit = x - 'A';
    if (digit <= 15) {
        return (digit / 3) + 2;
    }
    
    return ((digit - 1) / 3) + 2;
}

int is_valid(char* name, char* code) {
    int len = strlen(name);
    int i;

    for(i = 0; i < len; i++) {
        if(get_digit(name[i]) != code[i] - '0') {
            return 0;
        }
    }
    
    return 1;
}

int main () {
    FILE *fin  = fopen("namenum.in", "r");
    FILE *fout = fopen("namenum.out", "w");
    FILE *dict  = fopen("dict.txt", "r");

    char code[15];
    char name[15];
    size_t ln;

    fgets(code, 15, fin);
    ln = strlen(code) - 1;
    if (*code && code[ln] == '\n') 
        code[ln] = '\0';

    int has_name = 0;
    while(1) {
        if(fgets(name, 15, dict) == NULL) {
            break;
        }

        ln = strlen(name) - 1;
        if (*name && name[ln] == '\n') 
            name[ln] = '\0';

        if(strlen(name) != strlen(code)) {
            continue;
        }

        if(is_valid(name, code)) {
            fprintf(fout, "%s\n", name);
            has_name = 1;
        }
    }

    if(!has_name) {
        fprintf(fout, "NONE\n");
    }

    fclose(fin);
    fclose(fout);
    fclose(dict);
    return 0;
}
