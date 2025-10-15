// EG 7th family loop
// Prints a greeting for each family member or friend using a loop

#include <stdio.h>

int main(void) {
    char *names[] = {"Alice", "Bob", "Charlie", "Dana", "Eli"};
    int count = sizeof(names) / sizeof(names[0]);

    
    for (int i = 0; i < count; ++i) {
        printf("Hello, %s!\n", names[i]);
    }

    return 0;
}

