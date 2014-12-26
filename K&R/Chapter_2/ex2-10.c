#include <stdio.h>

int lower(int c) {
	return c >= 'A' && c <= 'Z' ? c + 'a' - 'A' : c;
}

int main() {
	int i;
	
	char test[] = "Hello, World!";

	for(i = 0; i < 13; i++) {
		printf("%c", lower(test[i]));
	}

	printf("\n%s\n", test);
}
