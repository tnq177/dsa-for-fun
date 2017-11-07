/*
ID: tnguye21
LANG: C
TASK: concom
*/

#include <stdio.h>
#include <stdlib.h>

// jk, i'm not MTP fan
struct company {
	int own[101];
	int not_own[101];
	int own_count;
	int not_own_count;
};

int n;
int com_count;
int list[100];
int visited[101];
struct company companies[101];
int percents[101][101];

int compare(const void* a, const void* b) {
    return ( *(int*)a - *(int*)b );
}

void check(int com) {
	while(1) {
		int has_new = 0;
		int i, j, not_own_com, p, temp;
		for(i = 0; i < companies[com].not_own_count; i++) {
			p = 0;
			not_own_com = companies[com].not_own[i];

			// printf("%d does not own %d\n", com, not_own_com);
			for(j = 0; j < companies[com].own_count; j++) {
				// printf("%d (belong to %d) owns %d %d percent", companies[com].own[j], com, not_own_com, percents[companies[com].own[j]][not_own_com]);
				p += percents[companies[com].own[j]][not_own_com];
			}
			if(p > 50) {
				temp = companies[com].not_own[i];
				companies[com].not_own[i] = companies[com].not_own[companies[com].not_own_count - 1];
				companies[com].not_own_count--;

				companies[com].own[companies[com].own_count] = temp;
				companies[com].own_count++;

				has_new = 1;
				break;
			}
		}

		if(!has_new) {
			break;
		}
	}
}

int main () {
    FILE *fin  = fopen ("concom.in", "r");
    FILE *fout = fopen ("concom.out", "w");

	int i, j;
    for(i = 1; i < 101; i++) {
    	visited[i] = 0;
    	companies[i].own_count = 0;
    	companies[i].not_own_count = 0;

    	for(j = 0; j < 101; j++) {
    		companies[i].own[j] = -1;
    		companies[i].not_own[j] = -1;

    		percents[i][j] = 0;
    	}
    }

	com_count = 0;
	fscanf(fin, "%d", &n);

	for(i = 0; i < n; i++) {
		int c1, c2, p;
		fscanf(fin, "%d %d %d", &c1, &c2, &p);

		if(!visited[c1]) {
			visited[c1] = 1;
			list[com_count] = c1;
			com_count++;
		}
		if(!visited[c2]) {
			visited[c2] = 1;
			list[com_count] = c2;
			com_count++;
		}

		percents[c1][c2] = p;
	}

	qsort(list, com_count, sizeof(int), compare);

	for(i = 0; i < com_count; i++) {
		for(j = 0; j < com_count; j++) {
			int c1, c2, p;
			c1 = list[i];
			c2 = list[j];
			p = percents[c1][c2];

			if(c1 == c2 || p > 50) {
				companies[c1].own[companies[c1].own_count] = c2;
				companies[c1].own_count++;
			}
			else {
				companies[c1].not_own[companies[c1].not_own_count] = c2;
				companies[c1].not_own_count++;
			}
		}
	}

	int com;
	for(i = 0; i < com_count; i++) {
		com = list[i];
		check(com);
		// print to file

		if(companies[com].own_count > 0) {
			qsort(companies[com].own, companies[com].own_count, sizeof(int), compare);

			for(j = 0; j < companies[com].own_count; j++) {
				if(com != companies[com].own[j]) {
					fprintf(fout, "%d %d\n", com, companies[com].own[j]);
				}
			}
		}
	}

    fclose(fin); 
    fclose(fout);
    return 0;
}
