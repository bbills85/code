#include <stdio.h>
#define MAXLINE 1000

int getline2(char line[], int maxline);
void reverse(char line[]);

int main() {
	char line[MAXLINE];

	while(getline2(line, MAXLINE) > 0) {
		reverse(line);
		printf("%s", line);
	}
	return 0;
}

int getline2(char s[], int lim) {
	int c, i, j;
	
	j = 0;
	for(i = 0; (c = getchar()) != EOF && c != '\n'; ++i)
		if(i < lim - 2) {
			s[j] = c;
			++j;
		}
	if(c == '\n') {
		s[j] = '\n';
		++j;
		++i;
	}
	s[j] = '\0';
	return i;
}

void reverse(char s[]) {
	int i, j, temp;

	i = 0;
	while(s[i] != '\0')
		++i;
	--i;
	if(s[i] == '\n')
		--i;
	j = 0;
	while(j < i) {
		temp = s[j];
		s[j] = s[i];
		s[i] = temp;
		++j;
		--i;
	}
}
