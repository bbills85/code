#include <stdio.h>

int main() {
	int i, z, t, main_array[5][5], *value, row = 0, column = 0, saddle = 0;

	srand(time(NULL));

	printf("\n\t+------------------------+\n\t¦");

	// Load 5x5 array with random values and display
	for(i = 0; i < 5; i++) {
		for(z = 0; z < 5; z++) {
			main_array[i][z] = (rand() % 55) + 11;
			printf(" %d ¦", main_array[i][z]);
		}
		if(i < 4)
			printf("\n\t+----+----+----+----+----+\n\t¦");
		else
			printf("\n\t+------------------------+\n\n");
	}

	// Used for debugging
/*	int main_array[5][5] = {
		{34, 51, 32, 41, 25} ,
                {14, 50, 43, 14, 31},
                {54, 52, 52, 42, 23},
                {33, 53, 51, 31, 35},
                {21, 54, 33, 13, 23}
	};*/

	for(i = 0; i < 5; i++) {
		for(z = 0; z < 5; z++) {
			value = &main_array[i][z];

			for(t = 0; t < 5; t++) {
				if(*value >= main_array[i][t]) 
					row++;
				if(*value <= main_array[t][z]) 
					column++;
		
				if(row == 5 && column == 5) {
					printf("\n\n\tSaddle point located at: %d\n", *value);
					saddle == 1;
				}
			}

		column = 0;
		row = 0;

		}
	}
//need to fix this part of the program
	if(saddle == 0)
		printf("\n\n\tNo saddle points! %d\n", saddle);
}
