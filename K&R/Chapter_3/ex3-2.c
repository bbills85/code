#include <stdio.h>
#include <string.h>

void escape(char s[], char t[]) {
	int i, n;

/*	for(i = 0, n = strlen(s); t[i] != '\0'; i++) {
		s[n++] = t[i];
		printf("im in s1: %c\n", s[n]);
		printf("im in s2: %c\n", t[i]);
	}
*/
	for(i = n = 0; t[i] != '\0'; i++) {
		switch(t[i]) {
			case '\t':
				s[n++] = '\\';
				s[n++] = 't';
				break;
			case '\n':
				s[n++] = '\\';
				s[n++] = 'n';
				break;
			default:
				s[n++] = t[i];
				break;
		}
	}
	s[n] = '\0';

	

	
}

int main() {
	char s1[] = "Hello";
	char s2[] = "wor\tld!\n\n";

	escape(s1, s2);

	printf("%s\n", s1);
}
