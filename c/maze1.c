/*
ID: tnguye21
LANG: C
TASK: maze1
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** maze;
int** adj_list;
int* adj_count;
int W, H;
int exits[2];

void get_farthest_distance(int exit, int** distances) {
	int* list;

	(*distances) = malloc(sizeof(int) * (W * H));
	list = malloc(sizeof(int) * (W * H));

	int i, j;
	for(i = 0; i < W * H; i++) {
		list[i] = i;
		(*distances)[i] = 1000000;
	}
	(*distances)[exit] = 0;

	int count = W * H;
	while(count > 0) {
		int min_dist, min_idx, list_idx;
		min_dist = 10000000;

		for(i = 0; i < count; i++) {
			int idx = list[i];
			if((*distances)[idx] < min_dist) {
				min_dist = (*distances)[idx];
				min_idx = idx;
				list_idx = i;
			}
		}

		// update neighbors
		for(j = 0; j < adj_count[min_idx]; j++) {
			int neighbor = adj_list[min_idx][j];
			(*distances)[neighbor] = (*distances)[neighbor] < min_dist + 1 ? (*distances)[neighbor] : min_dist + 1; 
		}

		// remove min_idx from list
		list[list_idx] = list[count - 1];
		count--;
	}
	free(list);
}

int main () {
    FILE *fin  = fopen ("maze1.in", "r");
    FILE *fout = fopen ("maze1.out", "w");

    fscanf(fin, "%d %d\n", &W, &H);
    adj_list = malloc(sizeof(int*) * (W * H));
    adj_count = malloc(sizeof(int) * (W * H));
    int i, j;
    for(i = 0; i < W * H; i++) {
    	adj_list[i] = malloc(sizeof(int) * 4);
    	adj_count[i] = 0;
    	for(j = 0; j < 4; j++) {
    		adj_list[i][j] = -1;
    	}
    }

    maze = malloc(sizeof(char*) * (2 * H + 1));
    for(i = 0; i < 2 * H + 1; i++) {
    	maze[i] = malloc(sizeof(char) * (2 * W + 1));
    }

    char *line = NULL;
    size_t len;
    int read;
    for(i = 0; i < 2 * H + 1; i++) {
    	read = getline(&line, &len, fin);
    	if(line[read - 1] == '\n') {
    		line[read - 1] = '\0';
    	}

    	strcpy(maze[i], line);
    }

    int exit_count = 0;
    for(i = 1; i < 2 * H + 1; i += 2) {
    	for(j = 1; j < 2 * W + 1; j += 2) {
    		int idx = (i / 2) * W + j / 2;

    		// check exits
    		int is_exit = (i == 1 && maze[i - 1][j] == ' ') || (i == 2 * H - 1 && maze[i + 1][j] == ' ') || (j == 1 && maze[i][j - 1] == ' ') || (j == 2 * W - 1 && maze[i][j + 1] == ' ');
			if(is_exit){    		
    			exits[exit_count] = idx;
    			exit_count++;
    		}

    		int neighbor = -1;
    		// north
    		if(i - 2 >= 0 && i - 2 < 2 * H + 1) {
    			if(maze[i - 1][j] == ' ') {
    				neighbor = ((i - 2) / 2) * W + j / 2;
					adj_list[idx][adj_count[idx]] = neighbor;
					adj_count[idx]++;
    			}
    		}	
    		// south
    		if(i + 2 >= 0 && i + 2 < 2 * H + 1) {
    			if(maze[i + 1][j] == ' ') {
    				neighbor = ((i + 2) / 2) * W + j / 2;
					adj_list[idx][adj_count[idx]] = neighbor;
					adj_count[idx]++;
    			}
    		}
    		// west
    		if(j - 2 >= 0 && j - 2 < 2 * W + 1) {
    			if(maze[i][j - 1] == ' ') {
    				neighbor = (i / 2) * W + (j - 2) / 2;
					adj_list[idx][adj_count[idx]] = neighbor;
					adj_count[idx]++;
    			}
    		}
    		// east
    		if(j + 2 >= 0 && j + 2 < 2 * W + 1) {
    			if(maze[i][j + 1] == ' ') {
    				neighbor = (i / 2) * W + (j + 2) / 2;
					adj_list[idx][adj_count[idx]] = neighbor;
					adj_count[idx]++;
    			}
    		}
    	}
    }

    int* distances_1;
    int* distances_2;

	get_farthest_distance(exits[0], &distances_1);
    if(exit_count == 2) {
		get_farthest_distance(exits[1], &distances_2);
    }

	int minimum_step = -1;
	for(i = 0; i < W * H; i++) {
		int min_step;
		if(exit_count == 2) {
			min_step = distances_1[i] < distances_2[i] ? distances_1[i] : distances_2[i];
		}
		else {
			min_step = distances_1[i];
		}
		minimum_step = minimum_step > min_step ? minimum_step : min_step;
	}
	fprintf(fout, "%d\n", minimum_step + 1);


    for(i = 0; i < 2 * H + 1; i++) {
    	free(maze[i]);
    }
    free(maze);
	free(distances_1);
	if(exit_count == 2) {
		free(distances_2);
	}
    for(i = 0; i < H; i++) {
    	free(adj_list[i]);
    }
    free(adj_list);

    fclose(fin); 
    fclose(fout);
    return 0;
}
