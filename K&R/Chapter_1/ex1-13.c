#include <stdio.h>

#define PRINT_BARS printf("#")
#define WORD_SIZE 10

int main() {
	int c, i, j, length, wordlength[WORD_SIZE];

	length = 0;

	for(i = 0; i < WORD_SIZE; ++i)
		wordlength[i] = 0;

	while((c = getchar()) != EOF) {
		if(c == ' ' || c == '\n' || c == '\t') {
			++wordlength[length];
			length = 0;
		}
		else
			++length;	
	}

	for(i = 0; i < WORD_SIZE; ++i) {
		printf("Words of size %d - ", i);
		for(j = 0; j < wordlength[i]; ++j) {
			if(wordlength[i] == 0)
				;
			else 
				PRINT_BARS;
		}
		printf("\n");
	}
}
