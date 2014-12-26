#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUMCAMERA 4

typedef struct vehicle {
    char reg[9];
    int camera;
    int time;
    struct vehicle *next;
} vehicle;

vehicle *start = NULL;
vehicle *current = NULL;

void convert(float *speed) {
    *speed = (*speed * 1.60934);
}

vehicle* find(vehicle *start, char *reg) {

    for (; start; start = start->next) {
        if (strcmp(reg, start->reg) == 0) 
            return start;
    }

    return NULL;
}

float find_speed(vehicle *start, vehicle *new) {
    vehicle *prev = find(start, new->reg);

    if(prev)
        return (new->time - prev->time);
    else
        return 0.0;
}

void update_car(char *line) {
    int hrs, mins, secs, total_time;
    float speed;

    vehicle *new = malloc(sizeof(vehicle));

    sscanf(line, "Vehicle %[^p] passed camera %i at %d:%d:%d", new->reg, &new->camera, &hrs, &mins, &secs);

    total_time = (hrs * 3600) + (mins * 60) + secs;

    new->time = total_time;
    new->next = NULL;

    printf("%s %i ", new->reg, new->camera);
    printf("%i\n", total_time);

//    speed = find_speed(start, new);

//    if (speed > 60) {
//        printf("Vehicle %s broke the speed limit by %f mph.", new->reg, speed);
//    }

    if(find(start, new->reg)) {
        return;
        printf("broken out");
    }

    printf("broken out didnt work");

    if (start == NULL) {
        printf("1 null\n");
        start = new;
        current = new;
    }
    else {
        printf("2 null\n");
        current->next = new;
        current = new;
    }
}

void display(vehicle *start) {
    vehicle *i = start;

    for (; i != NULL; i = i->next) {
        printf("Name: %s open: %d-%d\n", i->reg, i->camera, i->time);
    }
}

int main(int argc, char *argv[]) {
    char line[80], units[4];
    float speed_limit;
    int camera[NUMCAMERA], num_camera, start_pos = 0, loaded = 0;

    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
    }

    FILE *fp;

    if (!(fp = fopen(argv[1], "r"))) {
        fprintf(stderr, "Error: %s does not exist!\n", argv[1]);
        return 1;
    }

    fgets(line, sizeof(line), fp);

    sscanf(line, "Speed limit is %f %[^.]", &speed_limit, units);

//    if (!strstr(units, "mph"))
//        convert(&speed_limit);


    while (fgets(line, sizeof(line), fp) != NULL) { 
        if (sscanf(line, "Speed camera number %i is %i", &num_camera, &start_pos)) {
            camera[num_camera] = start_pos;
            printf("%i - %i\n", num_camera, camera[num_camera]);
        }
        if (strstr(line, "Vehicle")) {
              update_car(line);
        }
    }

    display(start);

    fclose(fp);
 
    return 0;
}
