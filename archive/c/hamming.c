/*
ID: tnguye21
LANG: C
TASK: hamming
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int is_connected(int x, int y, int D, int B) {
	int i = 0;
	int count = 0;
	int d1, d2;
	for(i = 0; i < B; i++) {
		d1 = x % 2;
		d2 = y % 2;
		x /= 2;
		y /= 2;

		if (d1 != d2) {
			count++;
		}
	}

	return (count >= D) ? 1 : 0;
}

int can_append_to_list(int i, int** list, int len, int*** adj_mat) {
    for(int j = 0; j < len; j++) {
        if(i == (*list)[j] || !(*adj_mat)[i][(*list)[j]]) {
            return 0;
        }
    }

    return 1;
}

void bfs(int i, int** list, int* idx, int** visited, int*** adj_mat, int** is_in_a_list, int num) {
    (*visited)[i] = 1;
    (*is_in_a_list)[i] = 1;
	(*list)[(*idx)] = i;
	(*idx)++;

	int j;
	for(j = 0; j < num; j++) {
		if(!(*visited)[j] && can_append_to_list(j, list, (*idx), adj_mat)) {
            bfs(j, list, idx, visited, adj_mat, is_in_a_list, num);
		}
	}
}

int compare(const void* a, const void* b) {
    return ( *(int*)a - *(int*)b );
}

int main () {
    FILE *fin  = fopen ("hamming.in", "r");
    FILE *fout = fopen ("hamming.out", "w");

    int N, B, D;
    int num;

    fscanf(fin, "%d %d %d", &N, &B, &D);
    num = (int)pow(2.0, B);

    int** adj_mat;
    int i, j;
    adj_mat = malloc(sizeof(int*) * num);
    for(i = 0; i < num; i++) {
    	adj_mat[i] = malloc(sizeof(int) * num);

    	for(j = 0; j < num; j++) {
    		adj_mat[i][j] = (i == j) ? 0 : is_connected(i, j, D, B);
    	}
    }

    int* is_in_a_list;
    is_in_a_list = malloc(sizeof(int) * num);
    for(i = 0; i < num; i++) {
        is_in_a_list[i] = 0;
    }

    for(i = 0; i < num; i++) {
        if(is_in_a_list[i]) {
            continue;
        }

    	int idx = 0;
    	int* list;
    	int* visited;
    	list = malloc(sizeof(int) * num);
    	visited = malloc(sizeof(int) * num);

    	for(j = 0; j < num; j++) {
    		visited[j] = 0;
            list[j] = -1;
    	}
    	bfs(i, &list, &idx, &visited, &adj_mat, &is_in_a_list, num);

        if (idx >= N - 1) {
            qsort(list, idx, sizeof(int), compare);
            int k;
            for(k = 0; k < N - 1; k++) {
                if((k + 1) % 10 == 0) {
                    fprintf(fout, "%d", list[k]);
                    fprintf(fout, "\n");
                }
                else {
                    fprintf(fout, "%d ", list[k]);
                }
            }
            fprintf(fout, "%d\n", list[N - 1]);

            free(list);
            free(visited);
            break;
        }

        free(list);
        free(visited);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
