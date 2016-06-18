/*
ID: tnguye21
LANG: C
TASK: milk3
*/

#include <stdio.h>
#include <stdlib.h>

int A, B, C;

void dfs(int**** visited, int a, int b, int c, int** result) {
    (*visited)[a][b][c] = 1;
    if(!a) {
        (*result)[c] = 1;
    }

    if(a) {
        // a --> b
        if(a + b >= B && !(*visited)[a + b - B][B][c]) {
            dfs(visited, a + b - B, B, c, result);
        }
        else if(a + b < B && !(*visited)[0][a + b][c]) {
            dfs(visited, 0, a + b, c, result);
        }

        // a --> c
        if(a + c >= C && !(*visited)[a + c - C][b][C]) {
            dfs(visited, a + c - C, b, C, result);
        }
        else if(a + c < C && !(*visited)[0][b][a + c]) {
            dfs(visited, 0, b, a + c, result);
        }
    }

    if(b) {
        // b --> a
        if(b + a >= A && !(*visited)[A][b + a - A][c]) {
            dfs(visited, A, b + a - A, c, result);
        }
        else if(b + a < A && !(*visited)[b + a][0][c]) {
            dfs(visited, b + a, 0, c, result);
        }

        // b --> c
        if(b + c >= C && !(*visited)[a][b + c - C][C]) {
            dfs(visited, a, b + c - C, C, result);
        }
        else if(b + c < C && !(*visited)[a][0][b + c]) {
            dfs(visited, a, 0, b + c, result);
        }
    }

    if(c) {
        // c --> a
        if(c + a >= A && !(*visited)[A][b][c + a - A]) {
            dfs(visited, A, b, c + a - A, result);
        }
        else if(c + a < A && !(*visited)[c + a][b][0]) {
            dfs(visited, c + a, b, 0, result);
        }

        // c --> b
        if(c + b >= B && !(*visited)[a][B][c + b - B]) {
            dfs(visited, a, B, c + b - B, result);
        }
        else if(c + b < B && !(*visited)[a][c + b][0]) {
            dfs(visited, a, c + b, 0, result);
        }
    }
}

int main () {
    FILE *fin  = fopen ("milk3.in", "r");
    FILE *fout = fopen ("milk3.out", "w");

    fscanf(fin, "%d", &A);
    fscanf(fin, "%d", &B);
    fscanf(fin, "%d", &C);

    int*** visited;
    visited = malloc(sizeof(int**) * (A + 1));
    int i, j, k;
    for(i = 0; i < A + 1; i++) {
        visited[i] = malloc(sizeof(int*) * (B + 1));
        for(j = 0; j < B + 1; j++) {
            visited[i][j] = malloc(sizeof(int) * (C + 1));

            for(k = 0; k < C + 1; k++) {
                visited[i][j][k] = 0;
            }
        }
    }

    int* result;
    result = malloc(sizeof(int) * (C + 1));
    for(i = 0; i < C + 1; i++) {
        result[i] = 0;
    }

    dfs(&visited, 0, 0, C, &result);

    char buffer[50];
    int length = 0;
    for(i = 0; i < C + 1; i++) {
        if(result[i]) {
            sprintf(buffer + length, "%d ", i);
            if (i < 10) {
                length += 2;
            }
            else {
                length += 3;
            }
        }
    }
    buffer[length - 1] = '\0';
    fprintf(fout, "%s\n", buffer);

    free(visited);
    free(result);
    fclose(fin);
    fclose(fout);
    return 0;
}
