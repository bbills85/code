#include <stdio.h>

int main() {
	int c, lastc;

	while((c = getchar()) != EOF) {
		if(c != ' ')
			putchar(c);
		if(c == ' ')
			if(lastc != ' ')
				putchar(c);
		lastc = c;	
	}
}
