#include <stdio.h>

/* print Fahrenheit-Celsius table
    for fahr = 0, 20, ..., 300; floating-point version */

float cel2fahr(float);
float fahr2cel(float);

float cel2fahr(float celsius) {
	return (9.0/5.0 * celsius) + 32.0;
}

float fahr2cel(float fahr) {
	return (5.0/9.0) * (fahr - 32.0);
}

main() {
	float fahr, celsius;
	int lower;

	printf("\n\tC/F-------Cel---Fahr-\n");
	printf("\n\t---------------------\n");

	celsius = lower;
	for(lower = 0; lower <= 300; lower += 20) {
		fahr = cel2fahr(lower);
		celsius = fahr2cel(lower);
		printf("\t%3d \t%6.1f %4.f\n", lower, celsius, fahr);
	}
}
