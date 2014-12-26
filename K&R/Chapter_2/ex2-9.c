#include <stdio.h>

int main() {
	int b, x;

	x = 15;

	for(b = 0; x != 0; x &= (x - 1))
		++b;

	printf("total 1 bits = %d\n", b);
}
