// EG 7TH name decorater
#include <stdio.h>
#include <string.h>

int main() {
    char name[100];
    char decoratedName[200];
    char decoration[] = "67";

    
    printf("Enter your name: ");
    scanf("%s", name);

    
    strcat(decoratedName, decoration);
    strcat(decoratedName, name);       
    strcat(decoratedName, decoration); 

    
    printf("Decorated Name: %s\n", decoratedName);

    return 0;
}