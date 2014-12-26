#include <stdio.h>
#include <string.h>

int main() {
    char str_a[20];  // A 20-element character array
    char *pointer;   // A pointer, meant for a character array
    char *pointer2;  // And yet another one

    strcpy(str_a, "Hello, world!\n");
    pointer = str_a;  // Set the first point to the start of the array
    printf(pointer);

    pointer2 = pointer + 2;  // Set the second one 2 bytes 
    printf(pointer2);        // Print it
    strcpy(pointer2, "y you guys!\n");  // Cope into that spot;
    printf(pointer);  // Print again

    return 0;
}
