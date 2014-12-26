#include <stdio.h>
#include <limits.h>
#include <float.h>

int main() {
	/* signed */
	printf("signed char min  = %d\n", SCHAR_MIN);
	printf("signed char max  = %d\n", SCHAR_MAX);
	printf("signed short min = %d\n", SHRT_MIN);
	printf("signed short max = %d\n", SHRT_MAX);
	printf("signed int min   = %d\n", INT_MIN);
	printf("signed int max   = %d\n", INT_MAX);
	printf("signed long min  = %ld\n", LONG_MIN);
	printf("signed long max  = %ld\n\n", LONG_MAX);
	/* unsigned */
	printf("unsigned char max  = %u\n", UCHAR_MAX);
	printf("unsigned short max = %u\n", USHRT_MAX);
	printf("unsigned int max   = %u\n", UINT_MAX);
	printf("unsigned long max  = %lu\n\n", ULONG_MAX);
	/* float */
	printf("float min = %e\n", FLT_MIN);
	printf("float max = %e\n", FLT_MAX);
	printf("double float min = %e\n", DBL_MIN);
	printf("double float max = %e\n", DBL_MAX);
	printf("long double float min = %Le\n", LDBL_MIN);
	printf("long double float max = %Le\n", LDBL_MAX);
}
