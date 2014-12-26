#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUMCAMERA 5 

typedef struct vehicle {
    char reg[9];
    int camera;
    float time;
    struct vehicle *next;
} vehicle;

vehicle *start = NULL;
vehicle *current = NULL;

int CAMERAS[NUMCAMERA];

void convert(float *speed) {
    *speed = (*speed * 1.60934);
}

float find(vehicle *start, vehicle *new) {

    int cam;
    float total;

    for (; start; start = start->next) {
        if (strcmp(new->reg, start->reg) == 0) {
            total = (new->time - start->time);
//            printf("%i %i %i", new->camera, start->camera, new->camera - start->camera);
            cam = (CAMERAS[new->camera] - CAMERAS[start->camera]);

            start->camera = new->camera;
            start->time = new->time;

//            printf("Name: %s\n", start->reg);
//            printf("Time: %f\n", total);
//            printf("Cam: %i\n", cam);

            return ((cam / total)  * 2.2369);
        }
    }

    return 0.0;
}

void update_car(char *line, float *speed_limit) {
    int hrs, mins, secs, total_time;
    float speed;

    vehicle *new = malloc(sizeof(vehicle));

    sscanf(line, "Vehicle %[^p] passed camera %i at %d:%d:%d", new->reg, &new->camera, &hrs, &mins, &secs);

    total_time = (hrs * 3600) + (mins * 60) + secs;

    new->time = total_time;
    new->next = NULL;
//printf("time - %f\n", new->time);
//    printf("%s %i ", new->reg, new->camera);
//    printf("%i\n", total_time);

    speed = find(start, new);

//    printf("%f", speed);

    if (speed) {
//        speed = find_speed(start, new);
//        printf("\n%f\n", speed);
        if (speed > *speed_limit) {
            printf("Vehicle %s broke the speed limit by %.1f mph.\n", new->reg, (speed - *speed_limit));
        }
        free(new);
        return;
    }

    if (start == NULL) {
        start = new;
        current = new;
    }
    else {
        current->next = new;
        current = new;
    }
}

void display(vehicle *start) {
    vehicle *i = start;

    for (; i != NULL; i = i->next) {
        printf("Name: %s open: %d-%f\n", i->reg, i->camera, i->time);
    }
}

void release(vehicle *start) {
    vehicle *i = start;
    vehicle *next = NULL;

    for(; i != NULL; i = next) {
        next = i->next;
        free(i);
    }

}

int main(int argc, char *argv[]) {
    char line[80], units[4];
    float speed_limit;
    int num_camera, start_pos = 0, loaded = 0;

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
            CAMERAS[num_camera] = start_pos;
        }
        if (strstr(line, "Vehicle")) {
            update_car(line, &speed_limit);
        }
    }

//    display(start);
    release(start);

    fclose(fp);
 
    return 0;
}
