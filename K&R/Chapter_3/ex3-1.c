#include <stdio.h>

int binsearch(int x, int v[], int n) {
	int low, high, mid;

	low = 0;
	high = n - 1;
	mid = (low + high) / 2;
	while(x != v[mid] && low <= high) {
		if(x > v[mid]) 
			low = mid + 1;	
		else
			high = mid - 1;
		mid = (low + high) / 2;
	}
	if(x == v[mid])
		return v[mid];
	else
		return -1;
}

int main() {
	int numbers[10] = { 8, 13, 15, 23, 27, 28, 68, 73, 86, 97 }, x;

	x = 15;

	printf("Number is %d\n", binsearch(x, numbers, 10));
}
