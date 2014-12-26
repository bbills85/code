#include <stdio.h>
int setbits(unsigned x, int p, int n, unsigned y) {
	return x & ~(~(~0 << n) << (p + 1 - n)) | (y & ~(~0 << n)) << p + 1 - n;
//	return (y & ~(~0 << n)) << p + 1 - n;
//	return x & ~(~(~0 << n) << p + 1 - n);// | (y & ~(~0 << n)) << p + 1 - n;
}

int main() {
	int x = 60;	/* 0011 1100 */
	int y = 125;	/* 0111 1101 */

	printf("%d\n", x);

	x = setbits(x, 6, 4, y);

	printf("%d\n", x);
}
