#include <stdio.h>
#define MAXLINE 1000

int getline2(char line[], int maxline);
int removeline(char line[], int len);

int main() {
	int len;
	char line[MAXLINE];

	while((len = getline2(line, MAXLINE)) > 0) {
		if(removeline(line, len) > 0)
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

int removeline(char s[], int len) {
	int i;

	i = 0;
	while(s[i] != '\n')
		++i;
	--i;
	while(i >= 0 && s[i] == ' ' || s[i] == '\t')
		--i;
	if(i >= 0) {
		++i;
		s[i] = '\n';
		++i;
		s[i] = '\0';
	}
	return i;
}
