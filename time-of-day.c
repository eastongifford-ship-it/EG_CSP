
// eg 7th time of day

#include <stdio.h>

int main() {
    int hour;

    // Ask user to enter the hour in military time
    printf("Enter the current hour (0–23): ");
    scanf("%d", &hour);

    // Greet based on input hour
    if (hour >= 18)
        printf("Good evening!\n");
    else if (hour >= 12)
        printf("Good afternoon!\n");
    else
        printf("Good morning!\n");

    return 0;
}