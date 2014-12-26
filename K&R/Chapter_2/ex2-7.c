#include <stdio.h>
int invert(unsigned x, int p, int n) {
	return x ^ (~(~0 << n) << (p + 1 - n));
}

int main() {
	int x = 60;	/* 0011 1100 */

	printf("%d\n", x);

	x = invert(x, 4, 4);

	printf("%d\n", x);
}
