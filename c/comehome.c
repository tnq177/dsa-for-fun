/*
ID: tnguye21
LANG: C
TASK: comehome
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int INF = 100000;
int NUM = 58;
int edges[58][58];
int list[58];
int visited[58];
int list_count;

int min(int x, int y) {
    return x < y ? x : y;
}

int main () {
    FILE *fin  = fopen ("comehome.in", "r");
    FILE *fout = fopen ("comehome.out", "w");

    int i, j;
    for(i = 0; i < NUM; i++) {
        list[i] = -1;
        visited[i] = 0;
        for(j = 0; j < NUM; j++) {
            edges[i][j] = INF;
        }
    }

    int P;
    fscanf(fin, "%d\n", &P);

    list_count = 0;
    for(i = 0; i < P; i++) {
        int b1, b2, e;
        char _b1, _b2;
        fscanf(fin, "%c %c %d\n", &_b1, &_b2, &e);
        b1 = _b1 - 'A';
        b2 = _b2 - 'A';
        edges[b1][b2] = min(edges[b1][b2], e);
        edges[b2][b1] = edges[b1][b2];

        if(!visited[b1]) {
            visited[b1] = 1;
            list[list_count] = b1;
            list_count++;
        }
        if(!visited[b2]) {
            visited[b2] = 1;
            list[list_count] = b2;
            list_count++;
        }
    }

    int distance[58];
    for(i = 0; i < 58; i++) {
        distance[i] = INF;
    }
    distance['Z' - 'A'] = 0;

    int old_list_count = list_count;
    while(list_count > 0) {
        int min_idx, min_dist, list_idx;
        min_dist = INF;
        for(i = 0; i < list_count; i++) {
            int idx = list[i];
            if(distance[idx] < min_dist) {
                min_dist = distance[idx];
                min_idx = idx;
                list_idx = i;
            }
        }

        list[list_idx] = list[list_count - 1];
        list[list_count - 1] = min_idx;
        list_count--;

        for(j = 0; j < NUM; j++) {
            distance[j] = min(distance[j], edges[j][min_idx] + min_dist);
        }
    }

    int min_cow, min_dist;
    min_dist = INF;
    for(i = 0; i < old_list_count; i++) {
        int idx = list[i];
        if(idx != ('Z' - 'A') && idx >=0 && idx < 26 && distance[idx] < min_dist) {
            min_dist = distance[idx];
            min_cow = idx;
        }
    }

    fprintf(fout, "%c %d\n", 'A' + min_cow, min_dist);
    fclose(fin); 
    fclose(fout);
    return 0;
}
