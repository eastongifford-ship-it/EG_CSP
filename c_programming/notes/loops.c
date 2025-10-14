// eg 7th loop notes
#include <stdio.h>
#include <string.h>



int main(void){
    int nums[] = {1,2,3,4,5,6,7,8,9,10}; // arrays
    char candies[][67]= {"67", "skittels", "smarties"};



    for(int x = 0; x < 10 ; x++){
        printf("%d\n",nums[x]);
    }
    for(int i = 0; i < 3; i++ ){
        printf("%s, is my favorite candy!\n", candies[i]);
    }

    int num = 1;
    while(num < 0){
        printf("%d\n", num);
        num++;
    }















    return 0;
}