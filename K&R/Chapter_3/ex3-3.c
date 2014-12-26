#include <stdio.h>
#include <string.h>

void expand(char s1[], char s2[]) {
	int i, n, j, start, end;

	j = 0;
	for(i = 0; s1[i] != '\0'; i++) {
		printf("%c\n", s1[i]);
		if(s1[i + 1] == '-') {
			start = (int) s1[i];
			end = (int) s1[i + 2];
			
			for(; start <= end; start++, j++) {
				printf("start = %d end = %d\n", start, end);
				s2[j] = (char) start;
			}
		}
	}
}

int main() {
	char s1[6] = "0-9-c";
	char s2[250] = "";

	expand(s1, s2);
	printf("%d %d\n", sizeof(s1), sizeof(s2));
	printf("s1 = %s\ns2 = %s\n", s1, s2);
}
