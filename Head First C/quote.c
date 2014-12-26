#include <stdio.h>

void cookie(char msg[]) {
    char s[] = "How big is it?";
    char *t = s;

    printf("%s\n", msg);
    printf("msg occupies %i bytes\n", sizeof(msg));
    printf("msg is %i large\n", sizeof(s));
    printf("The quote string is stored at: %p\n", msg);
}

int main() {
    char quote[] = "Cookies make you fat\0";

    cookie(quote);
}
