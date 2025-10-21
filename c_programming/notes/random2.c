// EG 7th random notes

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void){
    srand(time(NULL));
    
    
    for(int i=0; i<5; i++){
        int num = rand() % 67 +1;
        printf(" our random number is %d \n", num);
    }








    return 0;
}



