// EG 7th conditional notes
#include <stdio.h>
#include <string.h>
int main(void){

    int grade;
    char name[50];
    printf("what is your grade percentage? ");
    scanf("%d", &grade);
    printf("what is your name? ");
    scanf("%s", name);
    if (grade >= 90){
        printf("you got an A, %s\n", name);
    } else if (grade >= 80){
        printf("you got a B, %s\n", name);
    } else if (grade >= 70){
        printf("you got a C, %s\n", name);
    } else if (grade >= 60){
        printf("you got a D, %s\n", name);
    } else {
        printf("you got an F, %s\n", name);
    }







    return 0;
}

