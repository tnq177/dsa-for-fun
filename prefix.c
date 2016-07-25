/*
ID: tnguye21
LANG: C
TASK: prefix
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int MAX_SEQ_LENGTH = 200001;
int MAX_PREFIX_COUNT = 200;

char** prefixes;
int* prefix_lengths;
char* seq;
int prefix_count = 0;
int seq_length = 0;
int* d;

int max(int x, int y) {
    return x > y ? x : y;
}

int match(int i, int j) {
    int prefix_length = prefix_lengths[j];
    if(i + prefix_length > seq_length) {
        return 0;
    }

    int k;
    for(k = 1; k <= prefix_length; k++) {
        if(seq[i + k] != prefixes[j][k - 1]) {
            return 0;
        }
    }

    return 1;
}

int main() {
    FILE *fin  = fopen("prefix.in", "r");
    FILE *fout = fopen("prefix.out", "w");    

    prefix_lengths = malloc(sizeof(int) * MAX_PREFIX_COUNT);
    prefixes = malloc(sizeof(char*) * MAX_PREFIX_COUNT);
    int i;
    for(i = 0; i < MAX_PREFIX_COUNT; i++) {
        prefixes[i] = malloc(sizeof(char) * 11);
        memset(prefixes[i], '\0', 11);

        prefix_lengths[i] = -1;
    }

    seq = malloc(sizeof(char) * MAX_SEQ_LENGTH);
    memset(seq, '\0', MAX_SEQ_LENGTH);

    char *line = NULL;
    size_t len = 0;
    int read;
    char *tok;
    while((read = getline(&line, &len, fin)) != -1) {
        if(line[read - 1] == '\n') {
            line[read - 1] = '\0';
        }

        if(line[0] == '.') {
            break;
        }

        tok = strtok(line, " ");
        while(tok != NULL) {
            strcpy(prefixes[prefix_count], tok);
            prefix_lengths[prefix_count] = strlen(tok);
            prefix_count++;
            tok = strtok(NULL, " ");
        }
    }

    while((read = getline(&line, &len, fin)) != -1) {
        if(line[read - 1] == '\n') {
            line[read - 1] = '\0';
        }

        strcpy(seq + seq_length + 1, line);
        seq_length += read - 1;
    }

    d = malloc(sizeof(int) * (seq_length + 1));
    for(i = 0; i < seq_length + 1; i++) {
        d[i] = -1;
    }
    d[0] = 0;

    int j;
    for(i = 0; i < seq_length + 1; i++) {
        for(j = 0; j < prefix_count; j++) {
            if(d[i] != -1 && match(i, j)) {
                d[i + prefix_lengths[j]] = max(d[i + prefix_lengths[j]], d[i] + prefix_lengths[j]);
            }
        }
    }

    int max_length = -1;
    for(i = 0; i <= seq_length; i++) {
        max_length = max(max_length, d[i]);
    }

    fprintf(fout, "%d\n", max_length);

    free(d);
    free(seq);
    free(prefix_lengths);
    for(i = 0; i < MAX_PREFIX_COUNT; i++) {
        free(prefixes[i]);
    }
    free(prefixes);
    fclose(fin);
    fclose(fout);
    return 0;
}
