/*
ID: tnguye21
LANG: C
TASK: friday
*/

#include <stdio.h>
#include <stdlib.h>

int is_leap_year(int year) {
    if (year % 100 == 0 && year % 400 != 0) {
        return 0;
    }

    return (year % 4 == 0) ? 1 : 0;
}

int main () {
    FILE *fin  = fopen ("friday.in", "r");
    FILE *fout = fopen ("friday.out", "w");

    int N;
    int is_leap ;
    int i;
    int year;
    int month;
    int total_days_last_years;
    int total_days;
    int* count;

    int cum_sum[12] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
    
    fscanf(fin, "%d", &N);
    
    count = malloc(sizeof(int) * 7);
    for (i = 0; i < 7; i++) {
        count[i] = 0;
    }

    total_days_last_years = 0;
    for (i = 0; i < N; i++) {
        year = 1900 + i;
        is_leap = is_leap_year(year);

        for (month = 0; month < 12; month++) {
            total_days = total_days_last_years + cum_sum[month] + 13;
            if (month > 1 && is_leap) {
                total_days += 1;
            }

            count[(total_days - 1) % 7] += 1;
        }

        total_days_last_years += is_leap ? 366 : 365;
    }

    // yes!
    fprintf(fout, "%d ", count[5]);
    fprintf(fout, "%d ", count[6]);
    fprintf(fout, "%d ", count[0]);
    fprintf(fout, "%d ", count[1]);
    fprintf(fout, "%d ", count[2]);
    fprintf(fout, "%d ", count[3]);
    fprintf(fout, "%d", count[4]);
    fprintf(fout, "\n");
    free(count);
    return 0;
}
