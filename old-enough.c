// eg 7th old enough


#include <stdio.h>

int main() {
    int age;

    // Ask user for their age
    printf("Enter your age: ");
    scanf("%d", &age);

    // Check eligibility and print only one output
    if (age >= 18) {
        printf("You are old enough to vote.\n");
    } else if (age >= 16) {
        printf("You are old enough to drive.\n");
    } else if (age >= 15) {
        printf("You are old enough to get a learner's permit.\n");
    } else if (age >= 5) {
        printf("You are old enough to go to school.\n");
    } else {
        printf("You are not old enough for any listed activity.\n");
    }

    return 0;
}