#include <stdio.h>

#define YES	1
#define	NO	0

int htoi(char s[]) {
	int i, n, hexdigit, inhex;

	i = n = 0;
	if(s[i] == '0') {
		++i;
		if(s[i] == 'x' || s[i] == 'X')
			++i;
	}

	inhex = YES;
	for( ; inhex == YES; ++i) {
		if(s[i] >= '0' && s[i] <= '9') 
			hexdigit = s[i] - '0';
		else if(s[i] >= 'a' && s[i] <= 'f')
			hexdigit = s[i] - 'a' + 10;
		else if(s[i] >= 'A' && s[i] <= 'F')
			hexdigit = s[i] - 'A' + 10;
		else 
			inhex = NO;

		if(inhex) 
			n = 16 * n + hexdigit;
	}
	return n;
}

int main() {
	int i, c;
	char s[10];

	for(i = 0; (c = getchar()) != '\n'; ++i)
		s[i] = c;

	printf("%d\n", htoi(s));
}
