#include <stdio.h>

#define MAX_SIZE 81

int main() {
	int i, length = 0;
	char c[MAX_SIZE] = "haveanicedayfeedthedogchillout";

	for(i = 0; i < MAX_SIZE; i++) {
		if(length < 4) {
			putchar(c[i]);
			length++;
		}
		else {
			printf("\n");
			putchar(c[i]);
			length = 1;
		}
	}
}
