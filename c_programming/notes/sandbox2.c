#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

int main(void){
   
    
    int life(void){
        int lives = 6;
        if(lives == 6){
        printf("_____\n|    |\n|    |\n|    \n|    \n|_______\n");
        }else if(lives == 5){
        printf("_____\n|    |\n|    |\n|    o\n|    \n|_______\n");
        }else if(lives == 4){
        printf("_____\n|    |\n|    |\n|    o\n|   / \n|_______\n");
        }else if(lives == 3){
        printf("_____\n|    |\n|    |\n|    o\n|   /| \n|_______\n");
        }else if(lives == 2){
        printf("_____\n|    |\n|    |\n|    o\n|   /|\\ \n|_______\n");
        }else if(lives == 1){
        printf("_____\n|    |\n|    |\n|    o\n|   /|\\ \n|   /  \n|_______\n");
        }else{
        printf("_____\n|    |\n|    |\n|    o\n|   /|\\ \n|   / \\ \n|_______\n");
        }
        
    };
    life();
    
    return 0;
}



void choose_random_word() {
    srand(time(NULL));
	char words[60][30] = {"potato", "wagon", "cooperate", "seek", "sulphur", "center", "bounce", "ruin", "interference", "autonomy", "examination", "roof", "market", "pop", "light", "shock", "skin", "donor", "element", "execution", "vessel", "contrast", "coding", "python", "boring", "octopus"};
	int num = rand() % 8;
    char word[30] = words[num];
    char display[30];
    for(int i = 0; i < strlen(word); i++) {
        display[i] = '_';
    }
}
