/*
ID: tnguye21
LANG: C
TASK: castle
*/

#include <stdio.h>
#include <stdlib.h>

int rows, cols;
int room_count;
int max_room_size;
int new_max_room_size;
int* castle;
int* rooms;
int* room_sizes;
int walls, blocked;

int is_connected(int row, int col, int n_row, int n_col) {
    walls = castle[row * cols + col];

    // W
    blocked = walls % 2;
    walls /= 2;
    if(!blocked && n_row == row && n_col == col - 1) {
        return 1;
    }

    // N
    blocked = walls % 2;
    walls /= 2;
    if(!blocked && n_row == row - 1 && n_col == col) {
        return 1;
    }

    // E
    blocked = walls % 2;
    walls /= 2;
    if(!blocked && n_row == row && n_col == col + 1) {
        return 1;
    }

    // S
    blocked = walls % 2;
    walls /= 2;
    if(!blocked && n_row == row + 1 && n_col == col) {
        return 1;
    }    

    return 0;
}

int is_valid(int row, int col, int n_row, int n_col, int connected) {
    if (n_row < 0 || n_row >= rows || n_col < 0 || n_col >= cols) {
        return 0;
    }

    return connected ? is_connected(row, col, n_row, n_col) : !is_connected(row, col, n_row, n_col);
}

void find_connected(int node_idx) {
    rooms[node_idx] = room_count;

    int row, col;
    int n_row, n_col;
    row = node_idx / cols;
    col = node_idx - row * cols;

    // West neighbor
    n_row = row;
    n_col = col - 1;
    if (is_valid(row, col, n_row, n_col, 1)) {
        if (!rooms[n_row * cols + n_col]) {
            find_connected(n_row * cols + n_col);
        }
    }
    // North neighbor
    n_row = row - 1;
    n_col = col;
    if (is_valid(row, col, n_row, n_col, 1)) {
        if (!rooms[n_row * cols + n_col]) {
            find_connected(n_row * cols + n_col);
        }
    }
    // East neighbor
    n_row = row;
    n_col = col + 1;
    if (is_valid(row, col, n_row, n_col, 1)) {
        if (!rooms[n_row * cols + n_col]) {
            find_connected(n_row * cols + n_col);
        }
    }
    // South neighbor
    n_row = row + 1;
    n_col = col;
    if (is_valid(row, col, n_row, n_col, 1)) {
        if (!rooms[n_row * cols + n_col]) {
            find_connected(n_row * cols + n_col);
        }
    }

}

int main () {
    FILE *fin  = fopen ("castle.in", "r");
    FILE *fout = fopen ("castle.out", "w");

    int i, j;
    int idx;
    int node_idx, neighbor_idx;
    int r, c, direction;
    int W, N, E, S;
    int temp_new_room_size;

    fscanf(fin, "%d %d", &cols, &rows);
    castle = malloc(sizeof(int) * (rows * cols));
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            idx = (i * cols) + j;
            fscanf(fin, "%d", &castle[idx]);
        }
    }

    rooms = malloc(sizeof(int) * (rows * cols));
    for (i = 0; i < rows * cols; i++) {
        rooms[i] = 0;
    }
    // Find room of each node
    room_count = 0;
    for (i = 0; i < rows * cols; i++) {
        if (!rooms[i]) {
            room_count++;
            find_connected(i);
        }
    }
    fprintf(fout, "%d\n", room_count);

    room_sizes = malloc(sizeof(int) * (room_count + 1));
    for (i = 0; i < room_count + 1; i++) {
        room_sizes[i] = 0;
    }
    for (i = 0; i < rows * cols; i++) {
        room_sizes[rooms[i]]++;
    }

    max_room_size = -1;
    for (i = 1; i < room_count + 1; i++) {
        if (room_sizes[i] > max_room_size) {
            max_room_size = room_sizes[i];
        }
    }
    fprintf(fout, "%d\n", max_room_size);

    new_max_room_size = -1;
    for (j = 0; j < cols; j++) {
        for (i = rows - 1; i >= 0; i--) {
            node_idx = i * cols + j;
            blocked = castle[node_idx];
            W = blocked % 2;
            blocked /= 2;
            N = blocked % 2;
            blocked /= 2;
            E = blocked % 2;
            blocked /= 2;
            S = blocked % 2;
            blocked /= 2;

            // W
            neighbor_idx = i * cols + j - 1;
            if(is_valid(i, j, i, j - 1, 0) && rooms[node_idx] != rooms[neighbor_idx]) {
                temp_new_room_size = room_sizes[rooms[node_idx]] + room_sizes[rooms[neighbor_idx]];
                if (temp_new_room_size > new_max_room_size) {
                    new_max_room_size = temp_new_room_size;
                    r = i + 1;
                    c = j + 1;
                    direction = 'W';
                }
            }
            // S
            neighbor_idx = (i + 1) * cols + j;
            if(is_valid(i, j, i + 1, j, 0) && rooms[node_idx] != rooms[neighbor_idx]) {
                temp_new_room_size = room_sizes[rooms[node_idx]] + room_sizes[rooms[neighbor_idx]];
                if (temp_new_room_size > new_max_room_size) {
                    new_max_room_size = temp_new_room_size;
                    r = i + 1;
                    c = j + 1;
                    direction = 'S';
                }
            }
            // N
            neighbor_idx = (i - 1) * cols + j;
            if(is_valid(i, j, i - 1, j, 0) && rooms[node_idx] != rooms[neighbor_idx]) {
                temp_new_room_size = room_sizes[rooms[node_idx]] + room_sizes[rooms[neighbor_idx]];
                if (temp_new_room_size > new_max_room_size) {
                    new_max_room_size = temp_new_room_size;
                    r = i + 1;
                    c = j + 1;
                    direction = 'N';
                }
            }
            // E
            neighbor_idx = i * cols + j + 1;
            if(is_valid(i, j, i, j + 1, 0) && rooms[node_idx] != rooms[neighbor_idx]) {
                temp_new_room_size = room_sizes[rooms[node_idx]] + room_sizes[rooms[neighbor_idx]];
                if (temp_new_room_size > new_max_room_size) {
                    new_max_room_size = temp_new_room_size;
                    r = i + 1;
                    c = j + 1;
                    direction = 'E';
                }
            }
        }
    }

    fprintf(fout, "%d\n", new_max_room_size);
    fprintf(fout, "%d %d %c\n", r, c, direction);

    free(castle);
    free(rooms);
    free(room_sizes);
    fclose(fin);
    fclose(fout);
    return 0;
}
