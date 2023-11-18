/*
ID: tnguye21
LANG: C
TASK: pprime
*/

// Yes, it's ugly.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int compare(const void* a, const void* b) {
    return ( *(long*)a - *(long*)b );
}

int is_prime(long x) {
    if(x <= 1) {
        return 0;
    }

    long i;
    for(i = 2; i * i <= x; i++) {
        if(x % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main () {
    FILE *fin  = fopen ("pprime.in", "r");
    FILE *fout = fopen ("pprime.out", "w");        

    long a, b;
    fscanf(fin, "%ld %ld", &a, &b);

    long* pprime;
    pprime = malloc(sizeof(long) * 1000000);
    int count = 0;
    long pali;
    long d1, d2, d3, d4, d5;
    for (d1 = 1; d1 <= 9; d1+=2) { 
        pali = d1;
        pprime[count] = pali;
        count++;
        
        // 2 digit
        pali = d1 * 10 + d1;
        pprime[count] = pali;
        count++;
        

        for (d2 = 0; d2 <= 9; d2++) {
            // 3 digit
            pali = d1 * 100 + d2 * 10 + d1;
            pprime[count] = pali;
            count++;
            

            // 4 digit
            pali = d1 * 1000 + d2 * 100 + d2 * 10 + d1;
            pprime[count] = pali;
            count++;
            

            for (d3 = 0; d3 <= 9; d3++) {
                // 5 digit
                pali = d1 * 10000 + d2 * 1000 + d3 * 100 + d2 * 10 + d1;
                pprime[count] = pali;
                count++;
                

                // 6 digit
                pali = d1 * 100000 + d2 * 10000 + d3 * 1000 + d3 * 100 + d2 * 10 + d1;
                pprime[count] = pali;
                count++;
                

                for (d4 = 0; d4 <= 9; d4++) {
                    // 7 digit
                    pali = d1 * 1000000 + d2 * 100000 + d3 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1;
                    pprime[count] = pali;
                    count++;
                    

                    // 8 digit
                    pali = d1 * 10000000 + d2 * 1000000 + d3 * 100000 + d4 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1;
                    pprime[count] = pali;
                    count++;
                    

                    for(d5 = 0; d5 <= 9; d5++) {
                        // 9 digit
                        pali = d1 * 100000000 + d2 * 10000000 + d3 * 1000000 + d4 * 100000 + d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1;
                        pprime[count] = pali;
                        count++;
                                            
                    }
                }
            }
        }
    }

    qsort(pprime, count, sizeof(long), compare);
    for(d1 = 0; d1 < count; d1++) {
        if(pprime[d1] > b) {
            break;
        }

        if(pprime[d1] >= a && is_prime(pprime[d1])) {
            fprintf(fout, "%ld\n", pprime[d1]);
        }
    }

    free(pprime);
    fclose(fin);
    fclose(fout);
    return 0;
}
