#include <stdio.h>
#include <string.h>

int char2decimal(char *num) {
    int i, last = 1001, roman = 0, total = 0;

    for (i = 0; i < strlen(num); i++) {
        while (num[i] == num[i + 1]) {
            if (++roman > 3)
                return -1;
            i++;
        }
        roman = 0;
    }

    for (i = 0; i < strlen(num); i++) {
        printf("%c", num[i]);
        if (num[i] == 'M') {
            if (last == 100) {
                total -= last;
                total += 1000 - last;
                last = 1000;
            }
            else if (last < 1000)
                return -1;
            else {
                total += 1000;
                last = 1000;
            }
        }
        else if (num[i] == 'D') {
            if (last == 100) {
                total -= last;
                total += 500 - last;
                last = 500;
            }
            else if (last < 500)
                return -1;
            else {
                total += 500;
                last = 500;
            }
        }
        else if (num[i] == 'C') {
            if (last == 10) {
                total -= last;
                total += 100 - last;
                last = 100;
            }
            else if (last < 100)
                return -1;
            else {
                total += 100;
                last = 100;
            }
        }
        else if (num[i] == 'L') {
            if (last == 10) {
                total -= last;
                total += 50 - last;
                last = 50;
            }
            else if (last < 50)
                return -1;
            else {
                total += 50;
                last = 50;
            }
        }
        else if (num[i] == 'X') {
            if (last == 1) {
                total -= last;
                total += 10 - last;
                last = 10;
            }
            else if (last < 10)
                return -1;
            else {
                total += 10;
                last = 10;
            }
        }
        else if (num[i] == 'V') {
            if (last == 1) {
                total -= last;
                total += 5 - last;
                last = 5;
            }
            else if (last < 5)
                return -1;
            else {
                total += 5;
                last = 5;
            }
        }
        else if (num[i] == 'I') {
            total += 1;
            last = 1;
        }
    }

    return total;
}


int main() {
//    char num[] = "(X)MMCCCXLV";
//    char num[] = "MMCCCXLV";
    char num[] = "DM";

    printf(" %d\n", char2decimal("XD"));
    printf(" %d\n", char2decimal("DM"));
    printf(" %d\n", char2decimal("IVIII"));
    printf(" %d\n", char2decimal("IIL"));
    printf(" %d\n", char2decimal("XIL"));
    printf(" %d\n", char2decimal("XLIXX"));
    printf(" %d\n", char2decimal("MCMLXXXIII"));

}
