#include <stdio.h>
int righttrot(unsigned x, int n) {
//	int i;

//	unsigned j = (unsigned) ~0;

//	for(i = 0; (j = j >> 1) > 0;i++)
		;
//	return i;

//	while(n > 0
//	return x << 5;
	return x & ((x >> n) | (x << (8 - n)));
}

int main() {
	int x = 60;	/* 0011 1100 */

	printf("%d\n", x);
	printf("%d\n", 60 & 1927);
	x = righttrot(x, 3);

	printf("%d\n", x);
}
