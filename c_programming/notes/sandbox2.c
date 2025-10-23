#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

int main(void){

    life();
}
int life(void){
    int lives = 6;
    if(lives == 6){
        printf("_____\n|    |\n|    |\n|    \n|    \n|    |_______\n");
    }else if(lives == 5){
        printf("_____\n|    |\n|    |\n|    o\n|    \n|    |_______\n");
    }else if(lives == 4){
        printf("_____\n|    |\n|    |\n|    o\n|   / \n|    |_______\n");
    }else if(lives == 3){
        printf("_____\n|    |\n|    |\n|    o\n|   /| \n|   |_______\n");
    }else if(lives == 2){
        printf("_____\n|    |\n|    |\n|    o\n|   /|\\ \n|    |_______\n");
    }else if(lives == 1){
        printf("_____\n|    |\n|    |\n|    o\n|   /|\\ \n|   /  \n|_______\n");
    }else{
        printf("_____\n|    |\n|    |\n|    o\n|   /|\\ \n|   / \\ \n|_______\n");
    }
}
