#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char *feeds[] = {"http://rss.nytimes.com/services/xml/rss/nyt/Americas.xml",
                     "http://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml",
                     "http://rss.nytimes.com/services/xml/rss/nyt/Europe.xml"};

    int times = 3;
    char *phrase = argv[1];
    int i;

    for (i = 0; i < times; i++) {
        char var[255];

        sprintf(var, "RSS_FEED=%s", feeds[i]);

        char *vars[] = {var, NULL};

        pid_t pid = fork();

        if (pid == -1) {
            fprintf(stderr, "Can't fork process: %s\n", strerror(errno));
            return 1;
        }

        if (!pid) {
            if (execle("/usr/bin/python", "/usr/bin/python", "./rssgossip.py", phrase, NULL, vars) == -1) {
                fprintf(stderr, "Can't run script: %s\n", strerror(errno));
                return 1;
            }
        }
    }

    return 0;
}
