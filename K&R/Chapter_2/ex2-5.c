#include <stdio.h>

int any(char s1[], char s2[]) {
	int i, j;

	for(i = 0; s1[i] != '\0'; i++)
		for(j = 0; s2[j] != '\0'; j++)
			if(s1[i] == s2[j])
				return i;
	return -1;
}

int main() {
	int loc = 0;
	char s1[] = "Hello,";
	char s2[] = " world!";

	printf("%s%s\n", s1, s2);

	loc = any(s1, s2);

	printf("s1 has the same characters starting at %d\n", loc);
}
