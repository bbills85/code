#include <stdio.h>

int main() {
	int c;
	double blanks = 0, tabs = 0, newlines = 0;

	while((c = getchar()) != EOF) {
		if(c == '\n')
			++newlines;
		if(c == '\t')
			++tabs;
		if(c == ' ')
			++blanks;
	}

	printf("Blanks - %.0f\nTabs - %.0f\nNewlines - %.0f\n", blanks, tabs, newlines);
}
