#include <stdio.h>

int main(void) {
    char name[50];  // buffer to store the name

    printf("What is your name? ");
    scanf("%49s", name);  // read up to 49 characters to avoid overflow

    printf("Hello, %s!\n", name);
    return 0;
}