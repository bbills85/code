#include <stdio.h>
#include <string.h>

int convert_month(char *month) {
    int i;

    const char *month_names[] = {
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    };

    for (i = 0; i < 12; i++) {
        if (strcmp(month_names[i], month) == 0)
            return i + 1;
    }
}

int expand_year(char *year) {
    int year_holder = atoi(year);

    if(year_holder >= 50 && year_holder <= 99)
        return (1900 + year_holder);
    else if(year_holder >= 0 && year_holder <= 49)
        return (2000 + year_holder);
    else
        return year_holder;
}

int main(int argc, char *argv[]) {
    char line[80], day[3], month[4], year[5];
    int num_month;

    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
    }

    FILE *fp;

    if (!(fp = fopen(argv[1], "r"))) {
        fprintf(stderr, "Error: %s does not exist!\n", argv[1]);
        return 1;
    }

    while (fgets(line, sizeof(line), fp) != NULL) { 
        if (line[4] == '-') {
            printf("%s", line);
        }
        else if (line[2] == '/') {
            sscanf(line, "%2s/%2s/%2s", month, day, year);
            printf("%i-%s-%s\n", expand_year(year), month, day);
        }
        else if (line[2] == '#') {
            sscanf(line, "%2s#%2s#%2s", month, year, day);
            printf("%i-%s-%s\n", expand_year(year), month, day);
        }
        else if (line[2] == '*') {
            sscanf(line, "%2s*%2s*%4s", day, month, year);
            printf("%s-%s-%s\n", year, month, day);
        }
        else if (line[3] = ' ') {
            sscanf(line, "%3s %2s, %4s", month, day, year);

            num_month = convert_month(month);

            if (num_month < 10)
                printf("%i-%02d-%s\n", expand_year(year), num_month, day);
            else
                printf("%i-%i-%s\n", expand_year(year), num_month, day);
        }
        else
            printf("Error: input error -> %s", line);
    }

    fclose(fp);
 
    return 0;
}
