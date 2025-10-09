
    // EG 7th String notes 
    
#include <stdio.h>
#include <string.h>
int main(void){
    char name[] = "Easton";
    
    char last_name[25];
    printf("tell me your last name: \n");
    scanf("%s", last_name);
    
    char full_name[50] = ""; 
    strcat(full_name, name);
    strcat(full_name, " "); 
    strcat(full_name, last_name);
    
    printf("[%s]\n", full_name);
    printf("your name is %s\n", full_name);
    printf("%c", last_name[0]);
    last_name[0] ='6';
    printf("%c", last_name[0]);
    last_name[0] ='7';
    printf("%c", last_name[0]);
    printf("your name is %s%s", name,  last_name);
    printf("%zu", strlen(full_name));
    printf("%zu", sizeof(full_name));






return 0;
}