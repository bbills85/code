#include <stdio.h>
#include <math.h>
#include <float.h>

#define PI 3.14159265358979323846264338327950288419716939937510L

int main() {
    int num, z = 0, n = 0, inside = 0;
    float rootxy, pii, x, y;

    printf("Enter number of decimal places for PI: ");
    scanf("%d", &num);

    printf("%.15Le\n", PI);

    return 0;
}
