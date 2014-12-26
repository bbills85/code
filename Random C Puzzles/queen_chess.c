#include <stdio.h>

int main() {	// Declare all required variables
	int i, z, queen1_row, queen1_column, queen2_row, queen2_column,
		chessBoard[8][8] = {
				{ 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0 },
		};

	srand(time(NULL));	// Set psuedorandom generator

	// Randomly set queen positions between 0 and 7
	queen1_row = rand() % 7;
	queen1_column = rand() % 7;
	queen2_row = rand() % 7;
	queen2_column = rand() % 7;

	// Set queen positions on chessBoard
	chessBoard[queen1_row][queen1_column] = 1;
	chessBoard[queen2_row][queen2_column] = 1;

	// Draw chessBoard
	printf("\n\n\t\t+-------------------------------+\n\t\t¦");

	for(i = 0; i < 8; i++) {
		for(z = 0; z < 8; z++) {
			printf(" %d ¦", chessBoard[i][z]);
		}
		if(i < 7)
			printf("\n\t\t+---+---+---+---+---+---+---+---+\n\t\t¦");
		else
			printf("\n\t\t+-------------------------------+\n\n");
	}

	// Test rows, columns, and diagonal
	if(queen1_row == queen2_row)
		printf("Queens can attack -- in the same row!!\n");
	else if(queen1_column == queen2_column)
		printf("Queens can attack -- in the same column!!\n");
	else if(((queen1_row - queen2_row) == (queen1_column - queen2_column)) ||
		 ((queen2_row - queen1_row) == (queen1_column - queen2_column)))
		printf("Queens can attack -- diagonally!!\n");
	else
		printf("Queens cannot attack!!\n");
}
