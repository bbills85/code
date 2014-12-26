#include <stdio.h>

int main() {
	int c;

	while((c = getchar()) != EOF) {
		if(c == ' ' || c == '\n' || c == '\t')
			printf("\n");
		else
			putchar(c);
	}
}
