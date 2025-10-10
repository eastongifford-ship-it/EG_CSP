// EG 7th silly sentences

#include <stdio.h>

int main(void) {
	char w1[50];
	char w2[50];
	char w3[50];

	printf("Enter the first word: ");
	scanf("%49s", w1);

	printf("Enter the second word: ");
	scanf("%49s", w2);

	printf("Enter the third word: ");
	scanf("%49s", w3);


	printf("The %s tried to %s the %s and everyone laughed.\n", w1, w2, w3);

	return 0;
}

