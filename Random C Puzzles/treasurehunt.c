#include <stdio.h>
#include <stdlib.h>

int main() {
	int number, array[5][5], i, z, noTreasure = 0;

	srand(time(NULL));

	printf("\n\n\t\t******************************************\n");
	printf("\t\t**\tWelcome to Treasure Hunter\t**\n");
	printf("\t\t**\t    By: William Sinkey    \t**\n");
	printf("\t\t******************************************\n\n");


	printf("\t\t\t    Your Treasure Map!\n");
	printf("\t\t\t+------------------------+\n");

	for(i = 0; i < 5; i++) {
		printf("\t\t\t|");
		for(z = 0; z < 5; z++) {
			number = rand() % (55 - 11 + 1) + 11;
			while(number / 10 > 5 || number % 10 > 5 || number % 10 == 0)
				number = rand() % (55 - 11 + 1) + 11;
			array[i][z] = number;
			printf(" %d |", number);
		}
		if(i < 4)
			printf("\n\t\t\t+----+----+----+----+----+\n");
		else
			printf("\n\t\t\t+------------------------+\n\n");
	}
	
	i = 0;
	z = 0;
	number = array[i][z];

	printf("\tYou have 25 chances starting at cell [1][1]: %d\n\n", number);

	while(noTreasure < 25) {
		if(((number / 10) == (i + 1)) && ((number % 10) == (z + 1))) {
			printf("\n\t\tYou found the treasure at cell [%d][%d]: %d!!\n\n", i + 1, z + 1, number);
			exit(0);
		}
		else {
			i = number / 10 - 1;
			z = number % 10 - 1;
			printf("\t%d) Now at cell [%d][%d]: %d\n", noTreasure + 1, i + 1, z + 1, number);
			number = array[i][z];
			noTreasure++;
		}
	}

	printf("\n\t\tSorry You Lose!\n\n");
}
