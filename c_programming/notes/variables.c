// EG 7th variable notes
#include <stdio.h>

int main(void){
   int grade = 95;// 4 bytes
   float pi = 3.14;// 4 bytes
   double long_pi= 3.14159265358; // 8 bytes
   char letter_grade = 'A'; // 1 byte
   char name[]= "Easton";
    printf("%s did it!", name);
    printf("You have a %d, in the class. That is an %c", grade, letter_grade);

    return 0;
}