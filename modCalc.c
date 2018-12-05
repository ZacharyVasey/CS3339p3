#include <stdio.h>

int main(int argc, int *argv[]){
	if (argc < 2){
		printf("\n\nPlease include 2 numbers in command line.\n\n");
		return 0;
	}

	float top;
	float bottom;
	float result;

	result = top / bottom;

	printf("\nYour result: %f", result);

	printf("\n\n");
	getchar();
	return 0;
}