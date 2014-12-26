#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// struct named island with the following variables
// pointer to struct called next
typedef struct island {
    char *name;
    char *opens;
    char *closes;
    struct island *next;
} island;

// function prototypes
island* create(char *name);
void display(island *start);
void release(island *start);

int main() {
    // setup struct pointers set to NULL
    island *start = NULL;
    island *i = NULL;
    island *next = NULL;

    char name[80];

    // for loop that checks until file is empty
    for(; fgets(name, 80, stdin) != NULL; i = next) {
        //set pointer next to what returns from function create
        next = create(name);
        // set pointer start to next, which is first struct on linked list
        if (start == NULL)
            start = next;
        // link remaining structs
        if (i != NULL)
            i->next = next;
    }

    display(start);
    release(start);

    return 0;
}

island* create(char *name) {
    island *i = malloc(sizeof(island));
    i->name = strdup(name);
    i->opens = "09:00";
    i->closes = "17:00";
    i->next = NULL;

    return i;
}

void display(island *start) {
    island *i = start;

    for (; i != NULL; i = i->next) {
        printf("Name: %s open: %s-%s\n", i->name, i->opens, i->closes);
    }
}

void release(island *start) {
    island *i = start;
    island *next = NULL;

    for(; i != NULL; i = NULL) {
        next = i->next;
        free(i->next);
        free(i);
    }
}
